import { useParams } from 'react-router-dom';
import Document from './Document';
import React from 'react';

function DocumentWrapper() {
    const params = useParams();
    return <Document params={params} />;
}

export default DocumentWrapper;
