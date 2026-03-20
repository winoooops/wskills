#!/usr/bin/env bash
#
# Eval Runner - Generate spawn commands for evals
#
# Usage:
#   ./generate_evals.sh /path/to/skill [iteration-name]
#
# This generates the commands to run. You copy-paste them or pipe to bash.
#

SKILL_PATH="${1:?Usage: $0 <skill-path> [iteration]}"
ITERATION="${2:-iteration-1}"
SKILL_NAME=$(basename "$SKILL_PATH")
WORKSPACE_DIR=$(dirname "$SKILL_PATH")/${SKILL_NAME}-workspace

EVALS_FILE="$SKILL_PATH/evals/evals.json"

if [[ ! -f "$EVALS_FILE" ]]; then
    echo "Error: $EVALS_FILE not found"
    exit 1
fi

# Create workspace dirs
mkdir -p "$WORKSPACE_DIR/$ITERATION"

echo "# Eval Runner for: $SKILL_NAME"
echo "# Workspace: $WORKSPACE_DIR/$ITERATION"
echo ""

# Read evals and generate commands
python3 - <<PYTHON
import json

with open("$EVALS_FILE") as f:
    data = json.load(f)

for eval_case in data.get("evals", []):
    eval_id = eval_case["id"]
    prompt = eval_case["prompt"]
    safe_name = "$SKILL_NAME".replace(" ", "-")[:30]
    task_name = f"eval-{eval_id}-{safe_name}"
    output_base = f"$WORKSPACE_DIR/$ITERATION/$task_name"
    
    # With skill
    echo "mkdir -p $output_base/with_skill"
    echo "# Eval $eval_id WITH skill: $prompt"
    
    # Without skill  
    echo "mkdir -p $output_base/without_skill"
    echo "# Eval $eval_id WITHOUT skill: $prompt"
    echo ""

echo "---"
echo "# Spawn commands (run these via sessions_spawn):"
echo ""

for eval_case in data.get("evals", []):
    eval_id = eval_case["id"]
    prompt = eval_case["prompt"]
    safe_name = "$SKILL_NAME".replace(" ", "-")[:30]
    task_name = f"eval-{eval_id}-{safe_name}"
    
    # With skill
    echo "sessions_spawn \"
    echo "  --agentId cthulhu \"
    echo "  --cwd $WORKSPACE_DIR/$ITERATION \"
    echo "  --label ${task_name}-with-skill \"
    echo "  --mode run \"
    echo "  --runtime subagent \"
    echo "  --task 'Execute this task: - Skill path: $SKILL_PATH - Task: $prompt - Save outputs to: $WORKSPACE_DIR/$ITERATION/$task_name/with_skill/output.txt'"
    echo ""
    
    # Without skill
    echo "sessions_spawn \"
    echo "  --agentId cthulhu \"
    echo "  --cwd $WORKSPACE_DIR/$ITERATION \"
    echo "  --label ${task_name}-without-skill \"
    echo "  --mode run \"
    echo "  --runtime subagent \"
    echo "  --task 'Execute this task (NO SKILL): - Task: $prompt - Save outputs to: $WORKSPACE_DIR/$ITERATION/$task_name/without_skill/output.txt'"
    echo ""
PYTHON
