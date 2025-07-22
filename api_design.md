## API Design for AlchemyOS

This document outlines the design of the RESTful API for AlchemyOS. The API will be used for communication between the different layers of the system and with the frontend.

### Authentication

All API endpoints will require authentication using JSON Web Tokens (JWT). The JWT will be passed in the `Authorization` header of each request.

### API Endpoints

#### 1. Knowledge Artifacts

- `GET /artifacts`: Get a list of all knowledge artifacts.
  - **Query Parameters:**
    - `status`: Filter artifacts by status (e.g., `draft`, `in_review`, `approved`).
    - `format`: Filter artifacts by format (e.g., `quote`, `micro-article`).
    - `tag`: Filter artifacts by tag.
  - **Response:**
    ```json
    [
      {
        "id": "uuid",
        "content": "This is a micro-article.",
        "format": "micro-article",
        "chaos_score": 5,
        "vibe": "Serious",
        "status": "approved",
        "created_at": "2023-10-27T10:00:00Z"
      }
    ]
    ```

- `GET /artifacts/{id}`: Get a specific knowledge artifact by ID.
  - **Response:**
    ```json
    {
      "id": "uuid",
      "content": "This is a micro-article.",
      "format": "micro-article",
      "chaos_score": 5,
      "vibe": "Serious",
      "status": "approved",
      "created_at": "2023-10-27T10:00:00Z",
      "tags": ["tag1", "tag2"],
      "history": [
        {
          "user": "user_id",
          "action": "created",
          "timestamp": "2023-10-27T10:00:00Z"
        },
        {
          "user": "user_id",
          "action": "approved",
          "timestamp": "2023-10-27T10:05:00Z"
        }
      ]
    }
    ```

- `POST /artifacts`: Create a new knowledge artifact.
  - **Request Body:**
    ```json
    {
      "raw_input": "Some raw input.",
      "format": "micro-article"
    }
    ```
  - **Response:**
    ```json
    {
      "id": "uuid",
      "content": "This is a newly generated micro-article.",
      "format": "micro-article",
      "chaos_score": 7,
      "vibe": "Contrarian",
      "status": "draft",
      "created_at": "2023-10-27T10:10:00Z"
    }
    ```

- `PUT /artifacts/{id}`: Update a knowledge artifact.
  - **Request Body:**
    ```json
    {
      "content": "This is the updated content of the micro-article."
    }
    ```

- `DELETE /artifacts/{id}`: Delete a knowledge artifact.

#### 2. Artifact Actions

- `POST /artifacts/{id}/approve`: Approve a knowledge artifact.
- `POST /artifacts/{id}/veto`: Veto a knowledge artifact.
- `POST /artifacts/{id}/schedule`: Schedule a knowledge artifact for distribution.
  - **Request Body:**
    ```json
    {
      "channel_id": "uuid",
      "scheduled_at": "2023-10-28T14:00:00Z"
    }
    ```

#### 3. Tags

- `GET /tags`: Get a list of all tags.
- `POST /tags`: Create a new tag.
  - **Request Body:**
    ```json
    {
      "name": "new-tag"
    }
    ```

#### 4. Users

- `GET /users`: Get a list of all users.
- `GET /users/{id}`: Get a specific user by ID.
- `PUT /users/{id}`: Update a user's role.
  - **Request Body:**
    ```json
    {
      "role": "sme"
    }
    ```

#### 5. Channels

- `GET /channels`: Get a list of all distribution channels.
- `POST /channels`: Create a new channel.
  - **Request Body:**
    ```json
    {
      "name": "new-channel",
      "type": "slack"
    }
    ```
