import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/homePage/HomePage";
import UserPage from "./pages/userPage/UserPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} /> 
          <Route path="/users/:userId" element={<UserPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
