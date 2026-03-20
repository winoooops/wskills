#!/usr/bin/env python3
"""
Generic Eval Runner - Run structured evals on any skill.

Usage:
    python eval_runner.py --skill-path /path/to/skill [--iteration iteration-1] [--ids 1,2,3]

Output:
    {skill}-workspace/{iteration}/results.json
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

def load_evals(skill_path: str) -> dict:
    """Load evals.json from the skill directory."""
    evals_file = Path(skill_path) / "evals" / "evals.json"
    if not evals_file.exists():
        print(f"Error: {evals_file} not found")
        sys.exit(1)
    
    with open(evals_file) as f:
        return json.load(f)

def create_workspace(skill_path: str, iteration: str) -> str:
    """Create workspace directory alongside the skill."""
    skill_name = Path(skill_path).name
    workspace = Path(skill_path).parent / f"{skill_name}-workspace" / iteration
    workspace.mkdir(parents=True, exist_ok=True)
    return str(workspace)

def sanitize_filename(text: str) -> str:
    """Convert text to safe filename."""
    return text.replace(" ", "-").replace("/", "-")[:50]

def build_task_prompt(eval_case: dict, skill_path: str, with_skill: bool) -> str:
    """Build the task prompt for subagent."""
    task = eval_case["prompt"]
    
    if with_skill:
        return f"""Execute this task:
- Skill path: {skill_path}
- Task: {task}
- Save outputs to: {{output_path}}"""
    else:
        return f"""Execute this task (NO SKILL - test without skill):
- Task: {task}
- Save outputs to: {{output_path}}"""

def run_subagent(prompt: str, cwd: str, label: str) -> dict:
    """Run a subagent and wait for completion."""
    import requests
    
    # This would integrate with OpenClaw's API
    # For now, we'll construct the proper command
    cmd = [
        "openclaw", "session", "spawn",
        "--agent", "cthulhu",
        "--mode", "run",
        "--runtime", "subagent",
        "--cwd", cwd,
        "--label", label,
        "--task", prompt
    ]
    
    # Note: Actual implementation would need OpenClaw API integration
    # This is a placeholder for the workflow
    return {"status": "spawned", "label": label}

def save_results(workspace: str, results: dict):
    """Save results to results.json."""
    results_file = Path(workspace) / "results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {results_file}")

def calculate_grades(results: dict) -> dict:
    """Calculate grading metrics."""
    grades = {
        "total_evals": len(results["evals"]),
        "with_skill": {"total_time": 0, "total_tokens": 0, "success": 0},
        "without_skill": {"total_time": 0, "total_tokens": 0, "success": 0},
        "improvements": []
    }
    
    for eval_result in results["evals"]:
        ws = eval_result.get("with_skill", {})
        wo = eval_result.get("without_skill", {})
        
        if ws.get("runtime") and wo.get("runtime"):
            time_improvement = (wo["runtime"] - ws["runtime"]) / wo["runtime"] * 100
            token_improvement = (wo["tokens"] - ws["tokens"]) / wo["tokens"] * 100
            
            grades["improvements"].append({
                "eval_id": eval_result["id"],
                "time_improvement_pct": round(time_improvement, 1),
                "token_improvement_pct": round(token_improvement, 1)
            })
        
        grades["with_skill"]["total_time"] += ws.get("runtime_ms", 0)
        grades["with_skill"]["total_tokens"] += ws.get("tokens", 0)
        grades["with_skill"]["success"] += 1 if ws.get("status") == "done" else 0
        
        grades["without_skill"]["total_time"] += wo.get("runtime_ms", 0)
        grades["without_skill"]["total_tokens"] += wo.get("tokens", 0)
        grades["without_skill"]["success"] += 1 if wo.get("status") == "done" else 0
    
    return grades

def main():
    parser = argparse.ArgumentParser(description="Run evals on any skill")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--iteration", default="iteration-1", help="Iteration name")
    parser.add_argument("--ids", help="Comma-separated eval IDs to run")
    parser.add_argument("--dry-run", action="store_true", help="Show what would run")
    
    args = parser.parse_args()
    
    # Load evals
    evals_data = load_evals(args.skill_path)
    skill_name = evals_data.get("skill_name", Path(args.skill_path).name)
    
    # Filter by IDs if specified
    evals = evals_data["evals"]
    if args.ids:
        target_ids = set(int(x) for x in args.ids.split(","))
        evals = [e for e in evals if e["id"] in target_ids]
    
    # Create workspace
    workspace = create_workspace(args.skill_path, args.iteration)
    print(f"Workspace: {workspace}")
    print(f"Running {len(evals)} evals for skill: {skill_name}")
    
    if args.dry_run:
        print("\nDry run - would run:")
        for eval_case in evals:
            print(f"  - Eval {eval_case['id']}: {eval_case['prompt'][:50]}...")
        return
    
    # This is where we'd spawn subagents
    # For now, print instructions
    print("\nTo run evals, tell me:")
    print(f"  'Run evals on {args.skill_path}'")
    print("\nI'll spawn subagents for each test case.")

if __name__ == "__main__":
    main()
