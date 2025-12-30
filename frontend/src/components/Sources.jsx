export default function Sources({ sources }) {
  if (!sources || sources.length === 0) return null;

  return (
    <div className="sources">
      <h3>Sources</h3>
      <ul>
        {sources.map((s, i) => (
          <li key={i}>
            <strong>{s.title}</strong>
            <p>{s.chunk_text}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
