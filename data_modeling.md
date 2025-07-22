## Data Modeling for AlchemyOS Knowledge Graph

### 1. Knowledge Artifact

This is the core table that stores all the generated content.

| Column Name      | Data Type        | Description                                                                                             |
| ---------------- | ---------------- | ------------------------------------------------------------------------------------------------------- |
| `id`             | `UUID`           | Primary key for the artifact.                                                                           |
| `raw_input`      | `TEXT`           | The original input that the artifact was generated from.                                                |
| `content`        | `TEXT`           | The generated content of the artifact.                                                                  |
| `format`         | `VARCHAR(255)`   | The format of the artifact (e.g., `quote`, `micro-article`, `visual`, `lightweight-app`, `automation`). |
| `chaos_score`    | `INTEGER`        | A score from 1-10 indicating the novelty/risk of the artifact.                                          |
| `vibe`           | `VARCHAR(255)`   | The vibe of the artifact (e.g., `Serious`, `Satire`, `Urgent`, `Contrarian`).                           |
| `half_life`      | `VARCHAR(255)`   | The half-life of the artifact (e.g., `Ephemeral`, `Evergreen`).                                         |
| `status`         | `VARCHAR(255)`   | The status of the artifact (e.g., `draft`, `in_review`, `approved`, `scheduled`, `posted`, `vetoed`).    |
| `created_at`     | `TIMESTAMP`      | The timestamp when the artifact was created.                                                            |
| `updated_at`     | `TIMESTAMP`      | The timestamp when the artifact was last updated.                                                       |
| `embedding`      | `VECTOR`         | The vector embedding of the artifact's content, used for similarity searches.                           |

### 2. Tag

This table stores the tags that are associated with each knowledge artifact.

| Column Name | Data Type      | Description                               |
| ----------- | -------------- | ----------------------------------------- |
| `id`        | `UUID`         | Primary key for the tag.                  |
| `name`      | `VARCHAR(255)` | The name of the tag (e.g., `topic`, `stakeholder`, `sensitivity`). |

### 3. ArtifactTag

This is a join table that links knowledge artifacts to tags.

| Column Name      | Data Type | Description                               |
| ---------------- | --------- | ----------------------------------------- |
| `artifact_id`    | `UUID`    | Foreign key to the `knowledge_artifact` table. |
| `tag_id`         | `UUID`    | Foreign key to the `tag` table.           |

### 4. User

This table stores the users of the system.

| Column Name  | Data Type      | Description                                                                 |
| ------------ | -------------- | --------------------------------------------------------------------------- |
| `id`         | `UUID`         | Primary key for the user.                                                   |
| `email`      | `VARCHAR(255)` | The user's email address.                                                   |
| `role`       | `VARCHAR(255)` | The user's role (e.g., `owner`, `admin`, `sme`, `approver`, `editor`, `general`). |
| `created_at` | `TIMESTAMP`    | The timestamp when the user was created.                                    |

### 5. ArtifactUser

This is a join table that links knowledge artifacts to users. This can be used to track who created, reviewed, approved, or vetoed an artifact.

| Column Name      | Data Type      | Description                               |
| ---------------- | -------------- | ----------------------------------------- |
| `artifact_id`    | `UUID`         | Foreign key to the `knowledge_artifact` table. |
| `user_id`        | `UUID`         | Foreign key to the `user` table.          |
| `action`         | `VARCHAR(255)` | The action the user took on the artifact (e.g., `created`, `reviewed`, `approved`, `vetoed`). |

### 6. Channel

This table stores the channels that the knowledge artifacts can be distributed to.

| Column Name | Data Type      | Description                               |
| ----------- | -------------- | ----------------------------------------- |
| `id`        | `UUID`         | Primary key for the channel.              |
| `name`      | `VARCHAR(255)` | The name of the channel (e.g., `slack`, `twitter`, `linkedin`). |

### 7. ArtifactChannel

This is a join table that links knowledge artifacts to channels.

| Column Name      | Data Type | Description                               |
| ---------------- | --------- | ----------------------------------------- |
| `artifact_id`    | `UUID`    | Foreign key to the `knowledge_artifact` table. |
| `channel_id`     | `UUID`    | Foreign key to the `channel` table.       |
| `posted_at`      | `TIMESTAMP` | The timestamp when the artifact was posted to the channel. |
