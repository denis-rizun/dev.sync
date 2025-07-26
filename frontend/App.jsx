import React from 'react';
import { Link } from 'react-router-dom';
import statusToTag from './utils/statusToTag';
import './styles/index.css';

const loginUser = { id: null };  // temp

const App = () => (
    <div className="pusher">
        <header className="ui inverted vertical masthead center aligned segment">
            <div className="ui container">
                <nav className="ui large secondary inverted pointing menu">
                    <Link to="/" className="active header item">Home</Link>
                    <Link to="/dashboard" className="header item">Dashboard</Link>
                    <Link to="/doc" className="header item">Documents</Link>
                    <a
                        href="https://github.com/denis-rizun/dev.sync"
                        className="header item"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Source
                    </a>
                    <a
                        href="https://github.com/denis-rizun"
                        className="header item"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Me
                    </a>
                </nav>
            </div>

            <div className="ui text container">
                <h1 className="ui inverted header">Dev.Synchronizer</h1>

                {loginUser?.id ? (
                    <Link to="/webhook" className="ui huge primary button center-button">
                        Dashboard
                    </Link>
                ) : (
                    <Link href="/login" className="ui huge primary button center-button">
                        Login
                    </Link>
                )}


            </div>
        </header>

        <section className="ui vertical stripe quote segment">
            <div className="ui equal width stackable internally celled grid">
                <div className="center aligned row">
                    <div className="column">
                        <h3>Automate CD-processes</h3>
                        <p>GitHub / GitLab are supported</p>
                    </div>
                    <div className="column">
                        <h3>Any hook has its status</h3>
                        <p>{[1, 2, 3, 4, 5, 6].map(statusToTag)}</p>
                    </div>
                </div>
            </div>
        </section>

        <section className="ui vertical stripe segment centered-block">
            <div className="ui text container">
                <h3 className="ui header">Open Source can get more?</h3>
                <p>The backend is based on FastAPI, SQLAlchemy, Celery, Redis.</p>
                <p>The frontend uses React, Semantic UI</p>
            </div>
        </section>
    </div>
);

export default App;
