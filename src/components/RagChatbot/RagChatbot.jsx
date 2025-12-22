import React, { useState, useEffect } from 'react';
import './RagChatbot.module.css';

const RagChatbot = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');

  // Function to get selected text
  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      setSelectedText(selectedText);
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message to chat
    const userMessage = { id: Date.now(), text: inputValue, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    const currentInput = inputValue;
    setInputValue('');
    setIsLoading(true);

    try {
      // Prepare the request payload
      const requestBody = {
        query: currentInput,
        top_k: 5,
        selected_text: selectedText || null
      };

      // Call the backend API
      const response = await fetch('http://localhost:8000/api/rag/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      // Add bot response to chat
      const botMessage = {
        id: Date.now() + 1,
        text: data.response,
        sender: 'bot',
        sources: data.sources
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = {
        id: Date.now() + 1,
        text: 'Sorry, I encountered an error processing your request. Please try again.',
        sender: 'bot'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="rag-chatbot-container">
      <div className="rag-chatbot-header">
        <h3>Physical AI & Robotics Assistant</h3>
        {selectedText && (
          <div className="selected-text-indicator">
            <small>Context: "{selectedText.substring(0, 50)}{selectedText.length > 50 ? '...' : ''}"</small>
          </div>
        )}
      </div>

      <div className="rag-chatbot-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <p>Hello! I'm your Physical AI & Humanoid Robotics course assistant.</p>
            <p>Ask me anything about the course content, and I'll provide answers based on the curriculum.</p>
          </div>
        ) : (
          messages.map((message) => (
            <div
              key={message.id}
              className={`message ${message.sender}-message`}
            >
              <div className="message-text">{message.text}</div>
              {message.sources && message.sources.length > 0 && (
                <div className="message-sources">
                  <details>
                    <summary>Sources</summary>
                    <ul>
                      {message.sources.map((source, idx) => (
                        <li key={idx}>
                          {source.content_snippet.substring(0, 100)}
                          {source.content_snippet.length > 100 ? '...' : ''}
                        </li>
                      ))}
                    </ul>
                  </details>
                </div>
              )}
            </div>
          ))
        )}

        {isLoading && (
          <div className="message bot-message">
            <div className="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
      </div>

      <div className="rag-chatbot-input">
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a question about the course content..."
          rows="3"
          disabled={isLoading}
        />
        <button
          onClick={handleSendMessage}
          disabled={!inputValue.trim() || isLoading}
          className="send-button"
        >
          {isLoading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </div>
  );
};

export default RagChatbot;