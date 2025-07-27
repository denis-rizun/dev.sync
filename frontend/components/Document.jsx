import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { PROJECT_NAME } from '../constants/index';
import { ADD_KEY_CMD, GEN_CODE } from '../constants/document';
import '../styles/document.css';
import Header from "./Header";
import Footer from "./Footer";

const loginUser = { id: null };

function Document({ params }) {
    const [subject, setSubject] = useState(params?.subject || 'qa');

    useEffect(() => {
        if (params?.subject) {
            setSubject(params.subject);
        }
    }, [params?.subject]);

    const renderContent = (subject) => {
        if (subject === 'webhook') {
            return (
                <div className="doc-section">
                    <h2 className="doc-title">
                        What is the Basic Concept of {PROJECT_NAME}
                    </h2>
                    <p>
                        A Git triggers a POST request to a specified URL when
                        certain events happen in a Git repository. For example,
                        on GitHub, you can configure webhooks in the project’s
                        Settings to notify external services about pushes, pull
                        requests, and more.
                    </p>
                    <p>
                        All Git services support webhooks. This allows actions
                        like automatic code deployment, incremental code checks,
                        and continuous integration. Many third-party
                        integrations (like Travis CI) use this mechanism.
                    </p>
                    <p className="doc-highlight">
                        This project, {PROJECT_NAME}, leverages this concept to
                        provide a web interface for generating webhook URLs and
                        specifying shell scripts to execute when hooks trigger.
                    </p>

                    <h3 className="doc-subtitle">
                        How to Use {PROJECT_NAME} After Installation?
                    </h3>
                    <p>
                        Step 1: <strong>Deploy this project locally</strong>.
                        Self-hosting is recommended for security reasons. Refer
                        to the README for deployment instructions.
                    </p>
                    <p>
                        Step 2: <strong>Add server information</strong>. When a
                        push occurs on Git, specify which servers should execute
                        actions. Configure IP, PORT, username, and Private Key (
                        <Link to="/doc/pkey">how to generate?</Link>). This
                        project uses SSH to run shell commands remotely.
                    </p>
                    <img
                        className="doc-image"
                        src="../assets/server.png"
                        alt="Server configuration screenshot"
                    />

                    <p>
                        Step 3: <strong>Add webhook from Git</strong>. Enter the
                        project name, branch to hook, and select the server(s)
                        from step 2 to run shell commands upon pushes.
                    </p>
                    <img
                        className="doc-image"
                        src="../assets/webhook.png"
                        alt="Webhook configuration screenshot"
                    />
                    <p className="doc-highlight">
                        <strong>
                            Finally, copy the webhook URL (first button on the
                            right) and add it to the Git project's Settings →
                            Webhooks section to activate it.
                        </strong>
                    </p>
                </div>
            );
        }

        if (subject === 'pkey') {
            return (
                <div className="doc-section">
                    <h2 className="doc-title">
                        How to Obtain a Private Key on Linux?
                    </h2>
                    <p>
                        This example shows how the user{' '}
                        <strong>denis-rizun</strong> logs into server{' '}
                        <strong>10.246.14.121</strong> and obtains an SSH
                        private key.
                    </p>
                    <p>
                        Step 1: <strong>Generate a key pair</strong>. Login to
                        Linux via SSH and navigate to <code>~/.ssh/</code>. Run
                        the <code>ssh-keygen</code> command as follows:
                    </p>
                    <pre className="doc-code">{GEN_CODE}</pre>

                    <p>
                        Note: I left the passphrase empty so Python SSH login
                        can be passwordless. Important: generate the key{' '}
                        <em>on the Linux server</em> you want to login to.
                    </p>

                    <p>
                        Step 2:{' '}
                        <strong>Add the public key to authorized_keys</strong>.
                    </p>
                    <pre className="doc-code">{ADD_KEY_CMD}</pre>

                    <p>
                        All done! Copy the contents of{' '}
                        <code>id_rsa_forwebhook</code> into your server's
                        Private Key field.
                    </p>
                    <p className="doc-warning">
                        <strong>
                            Keep your private key and credentials secure at all
                            times.
                        </strong>
                    </p>
                </div>
            );
        }

        return (
            <div className="doc-section">
                <h2 className="doc-title">Looking for more Open Source?</h2>
                <p>This is the documentation page.</p>
                <p>The backend is built with FastAPI, SQLAlchemy, Celery and Redis.</p>
                <p>The frontend uses React.</p>
                <p>Feel free to submit issues or pull requests.</p>
            </div>
        );
    };

    return (
        <div className="page">
            <Header loginUser={loginUser} />
            <div className="doc-page">
                <div className="doc-sidebar">
                    <Link
                        to="/doc/webhook"
                        className={`doc-link ${location.pathname.startsWith('/doc/webhook') ? 'active' : ''}`}
                    >
                        What is Dev.Synchronizer and How to Use It?
                    </Link>
                    <Link
                        to="/doc/pkey"
                        className={`doc-link ${location.pathname.startsWith('/doc/pkey') ? 'active' : ''}`}
                    >
                        How to Obtain SSH Private Key?
                    </Link>
                </div>
                <div className="doc-content">{renderContent(subject)}</div>
            </div>
            <Footer />
        </div>
    );
}

export default Document;
