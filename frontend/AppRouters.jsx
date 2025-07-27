import React from 'react';
import { Route, Routes } from 'react-router-dom';
import App from './App';
import Document from './components/Document';
import DocumentWrapper from './components/DocumentWrapper';
import AuthPage from "./components/Registration";

function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<App />} />
            <Route path="/login" element={<AuthPage />} />
            <Route path="/doc" element={<Document params={{}} />} />
            <Route path="/doc/:subject" element={<DocumentWrapper />} />
        </Routes>
    );
}

export default AppRoutes;
