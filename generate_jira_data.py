from faker import Faker
import pandas as pd
import numpy as np
import random
import os
from datetime import timedelta

# ============================================================
# CONFIGURATION
# ============================================================

fake = Faker("fr_FR")

# Pour obtenir toujours les mêmes données à chaque exécution
Faker.seed(42)
random.seed(42)
np.random.seed(42)

OUTPUT_DIR = "data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Volumes
NB_USERS = 50
NB_PROJECTS = 10
NB_ISSUES = 5000
NB_SPRINTS_PER_PROJECT = 8
NB_BOARDS = 12
NB_COMPONENTS_PER_PROJECT = 5
NB_COMMENTS = 8000
NB_WORKLOGS = 7000
NB_ISSUE_LINKS = 2500
NB_ATTACHMENTS = 3000


# ============================================================
# FONCTION UTILITAIRE
# ============================================================

def save_csv(dataframe, filename):
    path = os.path.join(OUTPUT_DIR, filename)

    dataframe.to_csv(
        path,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"[OK] {filename} -> {len(dataframe)} lignes")


# ============================================================
# 1. USERS
# ============================================================

print("\n=== USERS ===")

teams = [
    "Development",
    "Data",
    "QA",
    "DevOps",
    "UX/UI",
    "Project Management",
    "Business",
    "Security"
]

users = []

for i in range(1, NB_USERS + 1):

    first_name = fake.first_name()
    last_name = fake.last_name()

    users.append({
        "user_id": f"USR-{i:04d}",
        "username": f"user{i:04d}",
        "first_name": first_name,
        "last_name": last_name,
        "email": f"user{i:04d}@company.local",
        "team": random.choice(teams),
        "role": random.choice([
            "Developer",
            "Data Analyst",
            "QA Engineer",
            "DevOps Engineer",
            "Project Manager",
            "Product Owner",
            "Business Analyst"
        ]),
        "active": random.choices(
            [True, False],
            weights=[95, 5]
        )[0]
    })

df_users = pd.DataFrame(users)

save_csv(df_users, "users.csv")


# ============================================================
# 2. ISSUE TYPES
# ============================================================

print("\n=== ISSUE TYPES ===")

issue_types = [
    {
        "issue_type_id": 1,
        "issue_type_name": "Epic",
        "category": "Planning"
    },
    {
        "issue_type_id": 2,
        "issue_type_name": "Story",
        "category": "Development"
    },
    {
        "issue_type_id": 3,
        "issue_type_name": "Task",
        "category": "Development"
    },
    {
        "issue_type_id": 4,
        "issue_type_name": "Bug",
        "category": "Quality"
    },
    {
        "issue_type_id": 5,
        "issue_type_name": "Sub-task",
        "category": "Development"
    }
]

df_issue_types = pd.DataFrame(issue_types)

save_csv(df_issue_types, "issue_types.csv")


# ============================================================
# 3. PRIORITIES
# ============================================================

print("\n=== PRIORITIES ===")

priorities = [
    {"priority_id": 1, "priority_name": "Highest", "priority_level": 5},
    {"priority_id": 2, "priority_name": "High", "priority_level": 4},
    {"priority_id": 3, "priority_name": "Medium", "priority_level": 3},
    {"priority_id": 4, "priority_name": "Low", "priority_level": 2},
    {"priority_id": 5, "priority_name": "Lowest", "priority_level": 1}
]

df_priorities = pd.DataFrame(priorities)

save_csv(df_priorities, "priorities.csv")


# ============================================================
# 4. STATUSES
# ============================================================

print("\n=== STATUSES ===")

statuses = [
    {
        "status_id": 1,
        "status_name": "To Do",
        "status_category": "To Do"
    },
    {
        "status_id": 2,
        "status_name": "In Progress",
        "status_category": "In Progress"
    },
    {
        "status_id": 3,
        "status_name": "Testing",
        "status_category": "In Progress"
    },
    {
        "status_id": 4,
        "status_name": "Blocked",
        "status_category": "In Progress"
    },
    {
        "status_id": 5,
        "status_name": "Done",
        "status_category": "Done"
    },
    {
        "status_id": 6,
        "status_name": "Reopened",
        "status_category": "In Progress"
    }
]

df_statuses = pd.DataFrame(statuses)

save_csv(df_statuses, "statuses.csv")


# ============================================================
# 5. PROJECTS
# ============================================================

print("\n=== PROJECTS ===")

project_names = [
    "E-Commerce",
    "Application Mobile",
    "CRM",
    "Data Platform",
    "ERP",
    "Digital Banking",
    "Customer Portal",
    "BI Platform",
    "Cybersecurity",
    "Cloud Migration"
]

project_keys = [
    "ECOM",
    "MOB",
    "CRM",
    "DATA",
    "ERP",
    "BANK",
    "PORTAL",
    "BI",
    "SEC",
    "CLOUD"
]

project_managers = df_users[
    df_users["role"] == "Project Manager"
]["username"].tolist()

if not project_managers:
    project_managers = df_users["username"].tolist()

projects = []

for i in range(NB_PROJECTS):

    start_date = fake.date_between(
        start_date="-2y",
        end_date="-6m"
    )

    projects.append({
        "project_id": f"PROJ-{i + 1:03d}",
        "project_key": project_keys[i],
        "project_name": project_names[i],
        "project_type": random.choice([
            "Software",
            "Data",
            "Infrastructure",
            "Digital Transformation"
        ]),
        "project_manager": random.choice(project_managers),
        "start_date": start_date,
        "status": random.choice([
            "Active",
            "Active",
            "Active",
            "Completed"
        ])
    })

df_projects = pd.DataFrame(projects)

save_csv(df_projects, "projects.csv")


# ============================================================
# 6. COMPONENTS
# ============================================================

print("\n=== COMPONENTS ===")

component_names = [
    "Backend",
    "Frontend",
    "Database",
    "API",
    "Authentication",
    "Payment",
    "Infrastructure",
    "Reporting",
    "Security",
    "Mobile"
]

components = []

component_id = 1

for _, project in df_projects.iterrows():

    selected_components = random.sample(
        component_names,
        NB_COMPONENTS_PER_PROJECT
    )

    for component in selected_components:

        components.append({
            "component_id": f"COMP-{component_id:04d}",
            "project_key": project["project_key"],
            "component_name": component,
            "component_lead": random.choice(
                df_users["username"].tolist()
            )
        })

        component_id += 1

df_components = pd.DataFrame(components)

save_csv(df_components, "components.csv")


# ============================================================
# 7. LABELS
# ============================================================

print("\n=== LABELS ===")

labels = [
    "frontend",
    "backend",
    "database",
    "security",
    "urgent",
    "customer",
    "production",
    "technical-debt",
    "performance",
    "mobile",
    "api",
    "bug",
    "improvement",
    "data",
    "analytics"
]

labels_data = []

for i, label in enumerate(labels, start=1):

    labels_data.append({
        "label_id": f"LBL-{i:03d}",
        "label_name": label
    })

df_labels = pd.DataFrame(labels_data)

save_csv(df_labels, "labels.csv")


# ============================================================
# 8. BOARDS
# ============================================================

print("\n=== BOARDS ===")

boards = []

for i in range(1, NB_BOARDS + 1):

    project = random.choice(
        df_projects["project_key"].tolist()
    )

    boards.append({
        "board_id": f"BOARD-{i:03d}",
        "board_name": f"{project} Board",
        "project_key": project,
        "board_type": random.choice([
            "Scrum",
            "Kanban"
        ])
    })

df_boards = pd.DataFrame(boards)

save_csv(df_boards, "boards.csv")


# ============================================================
# 9. SPRINTS
# ============================================================

print("\n=== SPRINTS ===")

sprints = []

sprint_id = 1

for _, project in df_projects.iterrows():

    project_start = pd.to_datetime(
        project["start_date"]
    )

    for sprint_number in range(
        1,
        NB_SPRINTS_PER_PROJECT + 1
    ):

        start_date = (
            project_start +
            timedelta(days=(sprint_number - 1) * 14)
        )

        end_date = start_date + timedelta(days=13)

        sprints.append({
            "sprint_id": f"SPR-{sprint_id:04d}",
            "sprint_name": f"{project['project_key']} Sprint {sprint_number}",
            "project_key": project["project_key"],
            "board_id": random.choice(
                df_boards[
                    df_boards["project_key"] ==
                    project["project_key"]
                ]["board_id"].tolist()
            ) if len(
                df_boards[
                    df_boards["project_key"] ==
                    project["project_key"]
                ]
            ) > 0 else None,
            "start_date": start_date.date(),
            "end_date": end_date.date(),
            "goal": fake.sentence(nb_words=8),
            "sprint_status": random.choice([
                "Completed",
                "Completed",
                "Active"
            ])
        })

        sprint_id += 1

df_sprints = pd.DataFrame(sprints)

save_csv(df_sprints, "sprints.csv")


# ============================================================
# 10. ISSUES
# ============================================================

print("\n=== ISSUES ===")

issues = []

all_projects = df_projects[
    "project_key"
].tolist()

all_users = df_users[
    "username"
].tolist()

all_sprints = df_sprints[
    "sprint_id"
].tolist()

all_components = df_components[
    "component_id"
].tolist()

# Utilisateurs de développement
developers = df_users[
    df_users["role"].isin([
        "Developer",
        "Data Analyst",
        "QA Engineer",
        "DevOps Engineer"
    ])
]["username"].tolist()

if not developers:
    developers = all_users


# Scénarios de projet
project_profiles = {}

for project in all_projects:

    profile = random.choice([
        "high_performance",
        "normal",
        "at_risk"
    ])

    project_profiles[project] = profile


for i in range(1, NB_ISSUES + 1):

    project = random.choice(all_projects)

    profile = project_profiles[project]

    # Type de ticket
    issue_type = random.choices(
        [
            "Story",
            "Task",
            "Bug",
            "Epic",
            "Sub-task"
        ],
        weights=[
            40,
            25,
            20,
            5,
            10
        ]
    )[0]

    # Priorité
    if profile == "at_risk":

        priority = random.choices(
            [
                "Highest",
                "High",
                "Medium",
                "Low",
                "Lowest"
            ],
            weights=[
                15,
                35,
                35,
                10,
                5
            ]
        )[0]

    else:

        priority = random.choice([
            "Highest",
            "High",
            "Medium",
            "Low",
            "Lowest"
        ])

    # Statut selon le profil
    if profile == "high_performance":

        status = random.choices(
            [
                "To Do",
                "In Progress",
                "Testing",
                "Blocked",
                "Done",
                "Reopened"
            ],
            weights=[
                10,
                15,
                10,
                2,
                58,
                5
            ]
        )[0]

    elif profile == "at_risk":

        status = random.choices(
            [
                "To Do",
                "In Progress",
                "Testing",
                "Blocked",
                "Done",
                "Reopened"
            ],
            weights=[
                20,
                30,
                10,
                15,
                15,
                10
            ]
        )[0]

    else:

        status = random.choices(
            [
                "To Do",
                "In Progress",
                "Testing",
                "Blocked",
                "Done",
                "Reopened"
            ],
            weights=[
                20,
                25,
                10,
                5,
                35,
                5
            ]
        )[0]

    created_date = fake.date_between(
        start_date="-18m",
        end_date="today"
    )

    due_date = created_date + timedelta(
        days=random.randint(7, 90)
    )

    # Résolution cohérente
    if status == "Done":

        resolution_days = random.randint(
            1,
            60
        )

        resolved_date = created_date + timedelta(
            days=resolution_days
        )

        # Eviter une résolution dans le futur
        if resolved_date > pd.Timestamp.today().date():

            resolved_date = pd.Timestamp.today().date()

    else:

        resolved_date = None

    # Story points
    if issue_type in ["Bug", "Task", "Story", "Sub-task"]:

        story_points = random.choice([
            1,
            2,
            3,
            5,
            8,
            13,
            21
        ])

    else:

        story_points = None

    # Epic
    if issue_type == "Epic":

        epic_link = None

    else:

        epic_link = None

    # Sprint
    sprint = random.choice(all_sprints)

    issues.append({

        "issue_id": i,

        "issue_key":
            f"{project}-{i}",

        "project_key":
            project,

        "issue_type":
            issue_type,

        "summary":
            fake.sentence(nb_words=random.randint(5, 12)),

        "description":
            fake.text(max_nb_chars=250),

        "priority":
            priority,

        "status":
            status,

        "reporter":
            random.choice(all_users),

        "assignee":
            random.choice(developers),

        "created_date":
            created_date,

        "updated_date":
            fake.date_between(
                start_date=created_date,
                end_date="today"
            ),

        "due_date":
            due_date,

        "resolved_date":
            resolved_date,

        "story_points":
            story_points,

        "sprint_id":
            sprint,

        "component_id":
            random.choice(all_components),

        "label":
            random.choice(labels),

        "epic_link":
            epic_link,

        "environment":
            random.choice([
                "Development",
                "Testing",
                "Staging",
                "Production"
            ]),

        "resolution":
            "Done"
            if status == "Done"
            else None
    })


df_issues = pd.DataFrame(issues)

save_csv(df_issues, "issues.csv")


# ============================================================
# 11. EPICS
# ============================================================

print("\n=== EPICS ===")

epic_issues = df_issues[
    df_issues["issue_type"] == "Epic"
].copy()

epics = []

for _, epic in epic_issues.iterrows():

    epics.append({

        "epic_id":
            f"EPIC-{epic['issue_id']:05d}",

        "epic_issue_key":
            epic["issue_key"],

        "project_key":
            epic["project_key"],

        "epic_name":
            epic["summary"],

        "epic_status":
            epic["status"],

        "start_date":
            epic["created_date"],

        "target_date":
            epic["due_date"]
    })

df_epics = pd.DataFrame(epics)

save_csv(df_epics, "epics.csv")


# ============================================================
# 12. ASSIGN EPICS TO ISSUES
# ============================================================

print("\n=== EPIC LINKS ===")

epic_keys_by_project = {}

for project in all_projects:

    epic_keys_by_project[project] = \
        df_epics[
            df_epics["project_key"] == project
        ]["epic_issue_key"].tolist()


for index in df_issues.index:

    project = df_issues.loc[
        index,
        "project_key"
    ]

    issue_type = df_issues.loc[
        index,
        "issue_type"
    ]

    if issue_type != "Epic":

        available_epics = epic_keys_by_project.get(
            project,
            []
        )

        if available_epics:

            # Une partie des tickets appartient à un Epic
            if random.random() < 0.70:

                df_issues.loc[
                    index,
                    "epic_link"
                ] = random.choice(
                    available_epics
                )


save_csv(df_issues, "issues.csv")


# ============================================================
# 13. STATUS HISTORY
# ============================================================

print("\n=== STATUS HISTORY ===")

status_history = []

history_id = 1

for _, issue in df_issues.iterrows():

    created = pd.Timestamp(
        issue["created_date"]
    )

    final_status = issue["status"]

    # Parcours réaliste
    possible_flow = [
        "To Do",
        "In Progress",
        "Testing",
        "Done"
    ]

    # Nombre d'étapes
    if final_status == "To Do":
        flow = ["To Do"]

    elif final_status == "In Progress":
        flow = [
            "To Do",
            "In Progress"
        ]

    elif final_status == "Testing":
        flow = [
            "To Do",
            "In Progress",
            "Testing"
        ]

    elif final_status == "Blocked":
        flow = [
            "To Do",
            "In Progress",
            "Blocked"
        ]

    elif final_status == "Reopened":
        flow = [
            "To Do",
            "In Progress",
            "Testing",
            "Done",
            "Reopened"
        ]

    else:
        flow = possible_flow

    for j in range(len(flow)):

        if j == 0:

            old_status = None
            new_status = flow[j]

        else:

            old_status = flow[j - 1]
            new_status = flow[j]

        changed_date = (
            created +
            timedelta(days=j * random.randint(1, 7))
        )

        status_history.append({

            "history_id":
                history_id,

            "issue_key":
                issue["issue_key"],

            "old_status":
                old_status,

            "new_status":
                new_status,

            "changed_by":
                random.choice(all_users),

            "changed_date":
                changed_date.date()
        })

        history_id += 1

df_status_history = pd.DataFrame(
    status_history
)

save_csv(
    df_status_history,
    "status_history.csv"
)


# ============================================================
# 14. COMMENTS
# ============================================================

print("\n=== COMMENTS ===")

comments = []

comment_texts = [
    "Le développement avance correctement.",
    "Il faut vérifier ce comportement.",
    "Le problème est reproduit en environnement de test.",
    "Correction proposée dans la prochaine version.",
    "Le client demande une modification.",
    "La fonctionnalité est prête pour les tests.",
    "Attention au délai prévu.",
    "Besoin de plus d'informations.",
    "Le problème semble corrigé.",
    "Tests complémentaires nécessaires."
]

issue_keys = df_issues[
    "issue_key"
].tolist()

for i in range(1, NB_COMMENTS + 1):

    issue_key = random.choice(issue_keys)

    comment_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    comments.append({

        "comment_id":
            f"COM-{i:05d}",

        "issue_key":
            issue_key,

        "author":
            random.choice(all_users),

        "comment_date":
            comment_date,

        "comment":
            random.choice(comment_texts)
    })

df_comments = pd.DataFrame(comments)

save_csv(df_comments, "comments.csv")


# ============================================================
# 15. WORKLOGS
# ============================================================

print("\n=== WORKLOGS ===")

worklogs = []

for i in range(1, NB_WORKLOGS + 1):

    issue = df_issues.sample(
        1
    ).iloc[0]

    worklogs.append({

        "worklog_id":
            f"WL-{i:05d}",

        "issue_key":
            issue["issue_key"],

        "user":
            random.choice(developers),

        "work_date":
            fake.date_between(
                start_date=issue["created_date"],
                end_date="today"
            ),

        "time_spent_hours":
            round(
                random.uniform(
                    0.5,
                    8
                ),
                2
            ),

        "description":
            fake.sentence(nb_words=6)
    })

df_worklogs = pd.DataFrame(worklogs)

save_csv(df_worklogs, "worklogs.csv")


# ============================================================
# 16. ISSUE LINKS
# ============================================================

print("\n=== ISSUE LINKS ===")

link_types = [
    "blocks",
    "is blocked by",
    "duplicates",
    "is duplicated by",
    "relates to"
]

issue_links = []

for i in range(1, NB_ISSUE_LINKS + 1):

    source = random.choice(issue_keys)

    target = random.choice(issue_keys)

    # éviter un lien vers soi-même
    while target == source:
        target = random.choice(issue_keys)

    issue_links.append({

        "link_id":
            f"LINK-{i:05d}",

        "source_issue":
            source,

        "target_issue":
            target,

        "link_type":
            random.choice(link_types)
    })

df_issue_links = pd.DataFrame(
    issue_links
)

save_csv(
    df_issue_links,
    "issue_links.csv"
)


# ============================================================
# 17. CUSTOM FIELDS
# ============================================================

print("\n=== CUSTOM FIELDS ===")

custom_fields = []

custom_field_names = [
    "Story Points",
    "Business Value",
    "Customer Impact",
    "Risk Level",
    "Technical Complexity"
]

for i, issue in df_issues.iterrows():

    if random.random() < 0.8:

        custom_fields.append({

            "custom_field_id":
                f"CF-{i + 1:06d}",

            "issue_key":
                issue["issue_key"],

            "field_name":
                random.choice(
                    custom_field_names
                ),

            "field_value":
                random.choice([
                    "Low",
                    "Medium",
                    "High",
                    "Very High"
                ])
        })

df_custom_fields = pd.DataFrame(
    custom_fields
)

save_csv(
    df_custom_fields,
    "custom_fields.csv"
)


# ============================================================
# 18. ATTACHMENTS
# ============================================================

print("\n=== ATTACHMENTS ===")

attachments = []

file_types = [
    "pdf",
    "png",
    "jpg",
    "xlsx",
    "docx",
    "csv"
]

for i in range(1, NB_ATTACHMENTS + 1):

    issue_key = random.choice(
        issue_keys
    )

    extension = random.choice(
        file_types
    )

    attachments.append({

        "attachment_id":
            f"ATT-{i:05d}",

        "issue_key":
            issue_key,

        "filename":
            f"document_{i}.{extension}",

        "file_type":
            extension,

        "size_kb":
            random.randint(
                50,
                5000
            ),

        "uploaded_by":
            random.choice(all_users),

        "upload_date":
            fake.date_between(
                start_date="-1y",
                end_date="today"
            )
    })

df_attachments = pd.DataFrame(
    attachments
)

save_csv(
    df_attachments,
    "attachments.csv"
)


# ============================================================
# FIN
# ============================================================

print("\n" + "=" * 60)
print("GENERATION TERMINÉE")
print("=" * 60)

print(f"""
Dossier de sortie : {OUTPUT_DIR}/

Fichiers générés :
- users.csv
- projects.csv
- issue_types.csv
- priorities.csv
- statuses.csv
- issues.csv
- epics.csv
- sprints.csv
- boards.csv
- components.csv
- labels.csv
- status_history.csv
- comments.csv
- worklogs.csv
- issue_links.csv
- custom_fields.csv
- attachments.csv
""")

print("Tu peux maintenant importer ces fichiers dans Power BI.")