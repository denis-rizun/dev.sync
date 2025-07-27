import React from 'react';
import Header from './components/Header';
import { PROJECT_NAME } from './constants';
import { Link } from 'react-router-dom';
import statusToTag from './utils/statusToTag';
import Footer from './components/Footer';
import '/styles/main.css';
import { useFadeInOnScroll } from './hooks/FadeInOnScroll';
import {useAuth} from "./hooks/useAuth";
import {ToastContainer} from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

const App = () => {
    useFadeInOnScroll();
    const user = useAuth();

    return (
        <div className="page">
            <Header user={user} />
            <main className="main-section">
                <section className="hero-section">
                    <div className="hero-container">
                        <h1 className="hero-title">{PROJECT_NAME}</h1>

                        {user?.id ? (
                            <Link
                                to="/webhook"
                                className="btn btn-primary center-button"
                            >
                                Dashboard
                            </Link>
                        ) : (
                            <Link
                                to="/login"
                                className="btn btn-primary center-button"
                            >
                                Login
                            </Link>
                        )}
                    </div>
                </section>

                <section className="features-section fade-in">
                    <div className="features-grid">
                        <div className="feature-item">
                            <h3>Automate CI/CD-processes</h3>
                            <p>GitHub / GitLab are supported</p>
                        </div>
                        <div className="feature-item">
                            <h3>Any hook has its status</h3>
                            <p>{[1, 2, 3, 4, 5, 6].map(statusToTag)}</p>
                        </div>
                    </div>
                </section>
            </main>
            <Footer />
            <ToastContainer position="top-right" autoClose={3000} />
        </div>
    );
};

export default App;
