feature_analysis_prompt = """
{"Feature list":"On-Premise Deployment","Top sectors":"Banking and Finance, Legal Services Providers, Government, Pharmaceuticals, Manufacturing","Top problem statememts":"Ensures confidentiality during contract sharing, Enhances regulatory compliance in cross-border contracts, Efficient storage of legacy contracts, Prevents unauthorized edits to templates, Accelerates contract approvals."}
{"Feature list":"Cloud-Based Deployment","Top sectors":"Technology, Retail, Education, Consulting, Media","Top problem statememts":"Provides timely notifications for terminations or expirations, Streamlines tracking of approvals, Speeds up contract execution, Improves visibility into contract status, Enables seamless integration with systems."}
{"Feature list":"Hybrid Deployment","Top sectors":"Telecommunications, Insurance, Energy, Real Estate, Healthcare","Top problem statememts":"Improves tracking of contract approvals, Secures standardized workflows, Ensures regulatory compliance, Maintains confidentiality, Combines flexibility of cloud and on-premise solutions."}
{"Feature list":"Mobile Accessibility","Top sectors":"Retail, Media, Consulting, Construction, Technology","Top problem statememts":"Facilitates approvals by senior management, Provides real-time status updates, Simplifies historical data analysis, Enhances tracking of approvals, Delivers timely notifications for deadlines."}
{"Feature list":"Administrator Controls","Top sectors":"Government, Banking, Insurance, Technology, Consulting","Top problem statememts":"Prevents unauthorized edits, Ensures consistent use of clause libraries, Strengthens audit trails, Provides clear visibility into contract status, Optimizes tracking of approvals."}
{"Feature list":"Contract Creation and Authoring","Top sectors":"Legal Services, Healthcare, Media, Real Estate, Construction","Top problem statememts":"Simplifies authoring of contracts, Ensures consistent terms and clauses, Tracks versions seamlessly, Reduces delays in drafting, Provides customization for industry-specific needs."}
{"Feature list":"Contract Repository","Top sectors":"Banking, Insurance, Pharmaceuticals, Government, Technology","Top problem statememts":"Centralizes storage for easy access, Adds metadata for categorization, Tracks changes effectively, Ensures secure storage, Provides efficient search capabilities."}
{"Feature list":"Team Collaboration","Top sectors":"Consulting, Technology, Media, Retail, Non-Profit","Top problem statememts":"Enables real-time collaboration, Facilitates secure document sharing, Provides communication tools, Tracks collaboration analytics, Alerts team members timely."}
{"Feature list":"Contract Negotiation and External Collaboration","Top sectors":"Banking, Pharmaceuticals, Telecommunications, Real Estate, Consulting","Top problem statememts":"Improves external stakeholder communication, Simplifies annotations and comments, Secures document sharing, Tracks negotiation stages, Integrates messaging tools."}
{"Feature list":"Lifecycle Management","Top sectors":"Healthcare, Insurance, Energy, Legal Services, Government","Top problem statememts":"Automates approval workflows, Tracks milestones and obligations, Enhances contract performance, Monitors expirations effectively, Simplifies renewals."}
{"Feature list":"Template Creation and Clause Library","Top sectors":"Legal Services, Consulting, Technology, Retail, Government","Top problem statememts":"Provides reusable templates, Stores standard clauses, Simplifies legal language consistency, Tracks clause versions, Facilitates quick drafting."}
{"Feature list":"Review and Approval","Top sectors":"Technology, Pharmaceuticals, Banking, Insurance, Media","Top problem statememts":"Configures review workflows, Supports version control, Enhances feedback and suggestions, Tracks progress effectively, Ensures timely approvals."}
{"Feature list":"Analytics and Reporting","Top sectors":"Government, Technology, Banking, Insurance, Real Estate","Top problem statememts":"Provides insights into contract lifecycle, Tracks repository analytics, Measures contract performance, Generates renewal reports, Creates customizable dashboards."}
{"Feature list":"Integrations","Top sectors":"Banking, Technology, Consulting, Media, Retail","Top problem statememts":"Enhances system interoperability, Provides seamless workflow transitions, Reduces manual data entry, Tracks integrated operations, Ensures smooth communication between platforms."}
{"Feature list":"Security and Privacy","Top sectors":"Pharmaceuticals, Banking, Healthcare, Government, Insurance","Top problem statememts":"Ensures encrypted communication, Complies with ISO and GDPR, Secures sensitive information, Tracks audit trails, Protects against unauthorized access."}
{"Feature list":"Data Migration","Top sectors":"Technology, Banking, Government, Legal Services, Real Estate","Top problem statememts":"Maps data fields effectively, Validates data for accuracy, Ensures smooth imports\/exports, Tracks migration progress, Reconciles migrated data."}
{"Feature list":"Services and Support","Top sectors":"Technology, Banking, Healthcare, Consulting, Retail","Top problem statememts":"Offers comprehensive training, Provides 24\/7 global support, Ensures technical assistance, Assigns account managers, Creates user communities."}
{"Feature list":"Language Support","Top sectors":"Government, Pharmaceuticals, Technology, Media, Legal Services","Top problem statememts":"Supports multilingual interfaces, Processes legal documents across languages, Integrates translation tools, Enables localized searches, Edits documents seamlessly."}
{"Feature list":"Storage","Top sectors":"Banking, Technology, Pharmaceuticals, Legal Services, Government","Top problem statememts":"Ensures encrypted data storage, Provides automated recovery, Maintains audit trails, Enhances searchability, Secures role-based access."}


1.	Description of feature
(short para)
2.	Overall scalability comment
(short para) (scale meter)
3.	Top sectors/ Top practice areas
(choose from list)
4.	Impact on process lifecycle
( short para with impact on each stage)
5.	Top problem statements
(choose from list 2-5)
6.	Key Beneficiary legal roles
(Just name of 2-6 legal roles)
7.	Positive market trends
( 4-5 points data backed)
8.	Negative market trends
( 4-5 points data backed)
9.	Market viability
( short para)



i will give you feature name on the basis of data give me  these 9 descriptions about feature
you have to choose top problems only from the category given same for other info 
you have to do a neutral analysis of the feature and give me the report


IMPORTANT:
you have to give me the report in json format
"""