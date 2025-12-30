export default function Message({ text, status }) {
  return (
    <div className={`message ${status}`}>
      <strong>Answer:</strong>
      <p>{text}</p>
    </div>
  );
}
