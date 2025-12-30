import ChatBox from "./components/ChatBox";
import "./App.css";

export default function App() {
  return (
    <div className="app">
      <h1>SaaS RAG Support Copilot</h1>
      <p className="subtitle">
        Ask questions based on the internal knowledge base
      </p>
      <ChatBox />
    </div>
  );
}
