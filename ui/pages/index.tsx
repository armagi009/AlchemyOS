import Head from "next/head";
import { useState } from "react";
import styles from "@/styles/Home.module.css";

export default function Home() {
  const [artifacts, setArtifacts] = useState([
    { id: 1, content: "This is the first artifact.", tags: ["tag1", "tag2"], approved: false },
    { id: 2, content: "This is the second artifact.", tags: ["tag2", "tag3"], approved: false },
  ]);
  const [chaosLevel, setChaosLevel] = useState(5);
  const [activityLog, setActivityLog] = useState([]);

  const handleMoreThis = (artifact) => {
    console.log("More of this:", artifact);
    logActivity(`Clicked 'More This' for artifact ${artifact.id}`);
  };

  const handleLessThis = (artifact) => {
    console.log("Less of this:", artifact);
    logActivity(`Clicked 'Less This' for artifact ${artifact.id}`);
  };

  const handleWtf = (artifact) => {
    console.log("WTF?!:", artifact);
    logActivity(`Clicked 'WTF?!' for artifact ${artifact.id}`);
  };

  const handlePanic = () => {
    console.log("Panic button pressed!");
    logActivity("Panic button pressed!");
  };

  const handleApprove = (id) => {
    setArtifacts(
      artifacts.map((artifact) =>
        artifact.id === id ? { ...artifact, approved: !artifact.approved } : artifact
      )
    );
    logActivity(`Toggled approval for artifact ${id}`);
  };

  const handleBulkApprove = () => {
    setArtifacts(artifacts.map(artifact => ({...artifact, approved: true})));
    logActivity("Bulk approved all artifacts");
  }

  const handleContentChange = (id, newContent) => {
    setArtifacts(
      artifacts.map((artifact) =>
        artifact.id === id ? { ...artifact, content: newContent } : artifact
      )
    );
    logActivity(`Edited artifact ${id}`);
  };

  const logActivity = (message) => {
    setActivityLog([...activityLog, { message, timestamp: new Date() }]);
  }

  return (
    <>
      <Head>
        <title>AlchemyOS</title>
        <meta name="description" content="AlchemyOS Dashboard" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className={styles.page}>
        <main className={styles.main}>
          <h1 className={styles.title}>AlchemyOS Dashboard</h1>
          <div className={styles.controls}>
            <button onClick={handlePanic} className={styles.panicButton}>
              Panic!
            </button>
            <button onClick={handleBulkApprove}>Bulk Approve</button>
            <div className={styles.chaosDial}>
              <label>Chaos Level: {chaosLevel}</label>
              <input
                type="range"
                min="1"
                max="10"
                value={chaosLevel}
                onChange={(e) => setChaosLevel(parseInt(e.target.value))}
              />
            </div>
          </div>
          <div className={styles.artifacts}>
            {artifacts.map((artifact) => (
              <div key={artifact.id} className={styles.artifact}>
                <textarea
                  value={artifact.content}
                  onChange={(e) => handleContentChange(artifact.id, e.target.value)}
                />
                <div className={styles.controls}>
                  <button onClick={() => handleMoreThis(artifact)}>More This</button>
                  <button onClick={() => handleLessThis(artifact)}>Less This</button>
                  <button onClick={() => handleWtf(artifact)}>WTF?!</button>
                  <button onClick={() => handleApprove(artifact.id)}>
                    {artifact.approved ? "Unapprove" : "Approve"}
                  </button>
                </div>
              </div>
            ))}
          </div>
          <div className={styles.activityLog}>
            <h2>Activity Log</h2>
            <ul>
              {activityLog.map((log, index) => (
                <li key={index}>
                  {log.timestamp.toLocaleTimeString()}: {log.message}
                </li>
              ))}
            </ul>
          </div>
        </main>
      </div>
    </>
  );
}
