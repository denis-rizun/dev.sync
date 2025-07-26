import React from 'react';

const statusToTag = (status) => {
    const statusMap = {
        1: { text: 'Waiting', color: 'olive' },
        2: { text: 'In Progress', color: 'yellow' },
        3: { text: 'Error', color: 'red' },
        4: { text: 'Success', color: 'green' },
        5: { text: 'Except', color: 'orange' },
    };

    const { text, color } = statusMap[status] || {
        text: 'Unknow',
        color: 'grey',
    };

    return (
        <span key={status} className={`compact ui mini tag label ${color}`}>
            {text}
        </span>
    );
};

export default statusToTag;
