import json
import re
def extract_json_from_string(string):
    # Use regex to find the JSON object in the string, including nested objects
    # Count opening and closing braces to handle nesting
    start = string.find('{')
    if start == -1:
        return {}
    
    count = 0
    for i in range(start, len(string)):
        if string[i] == '{':
            count += 1
        elif string[i] == '}':
            count -= 1
            if count == 0:
                try:
                    json_str = string[start:i+1]
                    # print(f"Extracted JSON: {json_str}")
                    return json.loads(json_str)
                except json.JSONDecodeError as e:
                    # print(f"JSON decode error: {e}")
                    return {}
    return {}



SAMPLE_REPORT= {
  "Current Status and Observations": {
    "High Exhaustion Levels in Critical Stages": "The stages with high exhaustion scores (4/5) include 'Draft Contract Terms,' 'Authenticate Contract Parties,' 'Execute Contract Agreement,' 'Store Contract Safely,' and 'Meeting.' These stages cover the entire lifecycle from drafting to execution, suggesting the team may be experiencing bottlenecks in essential contract handling steps.",
    "Workload Distribution": "Legal Managers, who represent more than half of the team, are heavily involved across all workflow steps. Paralegals, who could assist in more administrative tasks, may be underutilized based on the current task distribution.",
    "Repetitive Nature of Work": "Drafting and tracking contract terms (both rated 4/5 on repetitiveness) account for a significant amount of time and energy, likely contributing to delays and errors due to fatigue and redundancy."
  },
  "Quantitative Analysis of Losses": {
    "Average Time per Contract Cycle": "Assuming each stage takes an average of 3 hours for completion due to exhaustion and repetitiveness.",
    "Estimated Time Losses": {
      "Drafting": "4 hours x 4 reps x 10 Legal Managers = 160 hours/month",
      "Tracking Status": "3 hours x 4 reps x 10 Legal Managers = 120 hours/month",
      "Meetings": "1 hour per meeting, 3 reps x 18 participants = 54 hours/month",
      "Total Time Loss": "334 hours/month",
      "Productivity Loss": "This translates to approximately 41.75 full working days (assuming 8-hour workdays), equating to a monthly productivity loss of 20-25% for the team."
    }
  },
  "Red Flags": {
    "Overburdened Roles": "Legal Managers are engaged at every stage of the contract cycle, leading to high exhaustion and repetitive workload. This role overlap indicates inefficiencies and suggests the need for clearer task delegation to reduce workload strain.",
    "High Repetition in Non-Critical Stages": "High repetition scores in stages like 'Track Contract Status' and 'Meeting' indicate that resources are spent on non-core, time-consuming activities, lowering overall productivity and increasing burnout risks.",
    "Potential for Errors in Authentication and Execution": "High exhaustion scores in 'Authenticate Contract Parties' and 'Execute Contract Agreement' could lead to rushed work and overlooked details, posing risks of non-compliance, inaccuracies, and potential legal issues."
  },
  "Green Flags": {
    "Lifecycle Management Software": "The existing use of Lifecycle Management Software indicates that the team is aware of digital solutions and may be more receptive to additional technological integrations.",
    "Defined Workflow Stages": "The team has a well-outlined workflow from drafting to storage, creating a structured foundation on which automation and optimization can build."
  },
  "Data-Driven Recommendations and Solutions": {
    "Automation Potential": {
      "Automated Contract Drafting": "By implementing AI-powered contract drafting tools, the team can reduce drafting time by up to 40%.",
      "Expected Savings": "A 40% reduction in drafting hours (160 hours/month) would save approximately 64 hours/month, freeing up 8 workdays.",
      "Automated Status Tracking with Alerts": "Automated status tracking could eliminate the need for manual updates and reduce time spent on contract tracking by approximately 50%.",
      "Expected Savings": "A 50% reduction in tracking hours (120 hours/month) would save 60 hours/month, or 7.5 workdays.",
      "E-Signature for Authentication and Execution": "Implementing an e-signature solution can streamline both authentication and execution, cutting these times by 30-40% and significantly reducing exhaustion.",
      "Expected Savings": "A conservative 30% reduction in authentication and execution hours could save 36 hours/month, adding up to 4.5 workdays."
    },
    "Role Optimization": {
      "Task Delegation to Paralegals": "Paralegals should take on tracking and storage tasks, which are repetitive and could be easily managed with a standardized process.",
      "Expected Reduction in Legal Manager Time": "Delegating 50% of tracking and storage tasks to paralegals could free up 60 hours/month for Legal Managers, enabling them to focus on more strategic tasks.",
      "Centralized Communication for Meeting Efficiency": "Implementing a shared digital workspace for updates could reduce meeting frequency by 50%.",
      "Expected Savings": "A 50% reduction in meeting hours would save 27 hours/month (3.4 workdays) across the team."
    },
    "Enhancing Contract Analytics Usage": {
      "Contract Performance Insights": "Leveraging contract analytics more effectively can help track common bottlenecks, such as delays in contract execution and storage, enabling proactive intervention.",
      "Expected Outcome": "Reduction in delays and improved workflow continuity, particularly for high-exhaustion tasks like authentication and execution."
    }
  },
  "Scope for Improvement": {
    "Enhanced Use of Lifecycle Management": "By expanding the use of Lifecycle Management Software to include automated triggers and alerts, the team can further minimize manual monitoring efforts.",
    "Reduced Reliance on Meetings": "Moving to a digital dashboard for routine updates could replace 50-60% of repetitive meetings, focusing in-person meetings only on high-priority issues.",
    "Standardized Templates and Clause Library": "Creating templates for frequent contract types can reduce drafting time significantly and improve consistency, especially useful for paralegals and junior team members."
  },
  "Future Steps and Monitoring Metrics": {
    "Implementation Plan": {
      "1 Month": "Begin with e-signature adoption and contract tracking automation.",
      "3 Months": "Implement AI-driven drafting tools and delegate tracking/storage to paralegals.",
      "6 Months": "Fully integrate enhanced lifecycle management with analytics and develop standardized templates."
    },
    "Key Metrics for Success": {
      "Reduction in Repetitiveness and Exhaustion": {
        "Target": "30% reduction in repetitiveness for drafting and tracking by automating these processes.",
        "Exhaustion Score": "Aim to bring exhaustion scores to 2/5 or lower by redistributing tasks and automating high-frequency tasks."
      },
      "Time Saved per Month": {
        "Goal": "Track and compare monthly hours saved due to automation, aiming for a cumulative reduction of 200+ hours/month by six months."
      },
      "Improved Accuracy and Compliance": {
        "Goal": "Use contract analytics to monitor error rates in authentication and execution steps, aiming for a 25% reduction in errors within six months."
      }
    }
  }
}
