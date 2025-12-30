import { useState } from "react";
import { askRag } from "../api/rag";
import Message from "./Message";
import Sources from "./Sources";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleAsk() {
    if (!question.trim()) return;

    setLoading(true);
    setError("");
    setResponse(null);

    try {
      const data = await askRag(question);
      setResponse(data);
    } catch {
      setError("Failed to fetch answer");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="chat-box">
      <textarea
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {error && <p className="error">{error}</p>}

      {response && (
        <>
          <Message text={response.answer} status={response.status} />
          <Sources sources={response.sources} />
        </>
      )}
    </div>
  );
}
