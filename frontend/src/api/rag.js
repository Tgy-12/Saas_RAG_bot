const API_URL = "http://127.0.0.1:8000";

export async function askRag(question) {
  const response = await fetch(`${API_URL}/rag/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    throw new Error("RAG request failed");
  }

  return response.json();
}
