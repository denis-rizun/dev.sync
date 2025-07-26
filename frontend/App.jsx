import React from 'react';
import Header from './components/Header';
import { PROJECT_NAME } from './constants';
import { Link } from 'react-router-dom';
import statusToTag from './utils/statusToTag';
import Footer from './components/Footer';
import '/styles/main.css';
import { useFadeInOnScroll } from './hooks/FadeInOnScroll';

const loginUser = { id: null };

const App = () => {
    useFadeInOnScroll();

    return (
        <div className="page">
            <Header loginUser={loginUser} />
            <main className="main-section">
                <section className="hero-section">
                    <div className="hero-container">
                        <h1 className="hero-title">{PROJECT_NAME}</h1>

                        {loginUser?.id ? (
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
        </div>
    );
};

export default App;
