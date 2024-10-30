'use client'

import { PageContainer } from '@toolpad/core/PageContainer';
import Paper from '@mui/material/Paper';

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