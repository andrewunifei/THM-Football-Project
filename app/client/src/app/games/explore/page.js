'use client'

import { useState, useEffect } from 'react';
import { useSearchParams } from 'next/navigation'
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Divider from '@mui/material/Divider';
import TeamsGoalsPieChart from '@/app/components/teams/teamsGoalsPizza';
import TeamsBiggestTable from '@/app/components/teams/teamsBiggestTable';
import TeamsCardsSegment from '@/app/components/teams/teamsCardsSegment';
import TeamsGamesTable from '@/app/components/teams/teamsGamesTable';
import TeamsGoalsTable from '@/app/components/teams/teamsGoalsTable';
import TeamGamesPieChart from '@/app/components/teams/teamGamesPieChart';
import TeamsGoalsSegment from '@/app/components/teams/teamsGoalsSegment';
import { getTeamsGamesInfo, getTeamsGoalsInfo } from '@/app/api/team';
import { getTeamsCardsInfo } from '@/app/api/team';

function getTitle(logo, name) {
    return (
        <List sx={{ width: '100%', display: 'flex', alignItems:"flex-start"}} >
            <ListItem>
                <ListItemAvatar>
                    <Avatar alt="logo" src={logo}/>
                </ListItemAvatar>
                <p style={{fontSize: '34px', font: 'roboto', fontWeight: '100'}}>{name}</p>
            </ListItem>
        </List>
    )
}

function getBread() {
    return [
        {
            path: '/games',
            title: 'Jogos'
        },
        {
            path: '',
            title: 'Explorar'
        }
    ]
}
  
function ExploreGame() {
    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}> 
            <PageContainer maxWidth="xl" breadcrumbs={getBread()} sx={{marginBottom: '150px'}} >
                
            </PageContainer>
        </Paper>
    )
}

export default ExploreGame;