import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './AppRouters';
import {AuthProvider} from "./services/auth/AuthProvider";
import './styles/index.css';

const root = createRoot(document.getElementById('root'));

root.render(
    <BrowserRouter>
        {/*<AuthProvider>*/}
            <AppRoutes />
        {/*</AuthProvider>*/}
    </BrowserRouter>
);
