CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE knowledge_artifact (
    id UUID PRIMARY KEY,
    raw_input TEXT,
    content TEXT,
    format VARCHAR(255),
    chaos_score INTEGER,
    vibe VARCHAR(255),
    half_life VARCHAR(255),
    status VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    embedding VECTOR
);

CREATE TABLE tag (
    id UUID PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE artifact_tag (
    artifact_id UUID REFERENCES knowledge_artifact(id),
    tag_id UUID REFERENCES tag(id),
    PRIMARY KEY (artifact_id, tag_id)
);

CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    email VARCHAR(255),
    role VARCHAR(255),
    created_at TIMESTAMP
);

CREATE TABLE artifact_user (
    artifact_id UUID REFERENCES knowledge_artifact(id),
    user_id UUID REFERENCES "user"(id),
    action VARCHAR(255),
    PRIMARY KEY (artifact_id, user_id, action)
);

CREATE TABLE channel (
    id UUID PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE artifact_channel (
    artifact_id UUID REFERENCES knowledge_artifact(id),
    channel_id UUID REFERENCES channel(id),
    posted_at TIMESTAMP,
    PRIMARY KEY (artifact_id, channel_id)
);
