import React, { useState } from 'react';
import '../styles/login.css';
import Header from "./Header";
import Footer from "./Footer";
import { login } from "../services/auth/authService";
import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

const AuthPage = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [isLoginMode, setIsLoginMode] = useState(true);

    const handleAuth = async () => {
        try {
            const response = await login(username, password);
            toast.success(isLoginMode ? "Успешный вход!" : "Регистрация прошла успешно!");
            localStorage.setItem("access_token", response.data.access_token);
            window.location.href = "/";
        } catch (err) {
            console.log("Caught error:", err);

            if (err.response) {
                const status = err.response.status;
                console.log("Response status:", status);
                if (status === 403) {
                    toast.error("Неверный логин или пароль.");
                } else if (status === 500) {
                    toast.error("Внутренняя ошибка сервера.");
                } else {
                    toast.error(`Ошибка: код ${status}`);
                }
            } else if (err.request) {
                console.log("No response, but request sent:", err.request);
                toast.error("Сервер не отвечает.");
            } else {
                console.log("General error:", err.message);
                toast.error("Ошибка при отправке запроса.");
            }

            console.error("Auth error:", err);
        }
    };

    return (
        <div className="page">
            <Header />
            <div className="login-modal">
                <div className="login-menu">
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <button onClick={handleAuth}>
                        {isLoginMode ? "Login" : "Register"}
                    </button>
                </div>
                <div className="login-registration">
                    <p>
                        <b>
                            {isLoginMode ? "Don't have an account?" : "Already have an account?"}
                            <button
                                onClick={() => setIsLoginMode(!isLoginMode)}
                                style={{
                                    background: "none",
                                    border: "none",
                                    color: "#007bff",
                                    textDecoration: "underline",
                                    cursor: "pointer",
                                    paddingLeft: "6px"
                                }}
                            >
                                {isLoginMode ? "Register" : "Login"}
                            </button>
                        </b>
                    </p>
                </div>
            </div>
            <Footer />
            <ToastContainer position="top-right" autoClose={3000} />
        </div>
    );
};

export default AuthPage;
