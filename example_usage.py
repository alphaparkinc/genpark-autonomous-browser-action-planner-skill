from client import AutonomousBrowserActionPlannerClient

def main():
    client = AutonomousBrowserActionPlannerClient()
    res = client.plan_browser_actions()
    print("=== Autonomous Browser Action Planner Output ===")
    print(f"Goal: {res['goal']}")
    print(f"Plan ID: {res['action_plan_id']} | Total Steps: {res['total_actions']}")
    print("\nAction Steps Sequence:")
    for a in res['action_sequence']:
        print(f"  Step {a['step']}: {a['action_type']:<15} -> {a['selector']} ({a['description']})")

if __name__ == '__main__':
    main()
