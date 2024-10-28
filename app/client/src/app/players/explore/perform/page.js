'use client'

import { useState, useEffect } from 'react';
import { useSearchParams } from 'next/navigation'
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Avatar from '@mui/material/Avatar';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Divider from '@mui/material/Divider';

function getBread() {
    return [
        {
            path: '/players',
            title: 'Jogadores'
        },
        {
            path: '/players/explore',
            title: 'Explorar'
        },
        {
            path: '',
            title: 'Desempenho'
        }
    ]
}

function PlayerSingleGame() {
    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}> 
            <PageContainer maxWidth="xl" breadcrumbs={getBread()} sx={{marginBottom: '150px'}}>
            </PageContainer>
        </Paper>
    )
}

export default PlayerSingleGame