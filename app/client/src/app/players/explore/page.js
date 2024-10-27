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
import { getTeamsGamesInfo, getTeamsGoalsInfo } from '@/app/api/team';
import { getTeamsCardsInfo } from '@/app/api/team';
import { getPlayerInfo } from '@/app/api/player';

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
            path: '/players',
            title: 'Jogadores'
        },
        {
            path: '',
            title: 'Explorar'
        }
    ]
}

function ExplorePlayer() {
    const [ playerInfo, setPlayerInfo ] = useState({})
    const searchParams = useSearchParams();
    const player_id = searchParams.get('player-id')
    const name = searchParams.get('name')
    const photo = searchParams.get('photo')

    useEffect(() => {
        const fetchData = async () => {
            const playerData = await getPlayerInfo(player_id)
            setPlayerInfo(playerData)
          }
          fetchData();
    }, [])

    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}> 
            <PageContainer maxWidth="xl" breadcrumbs={getBread()} sx={{marginBottom: '150px'}} >
                {getTitle(photo, name)}
                <Grid container spacing={3} >
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                            <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Identificação Geral</p>
                            <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                            <p>
                                <span style={{fontWeight: 'bold'}}>Nome completo: </span>
                                {(playerInfo['first_name'] && playerInfo['last_name']) ? (playerInfo['first_name'] + ' ' + playerInfo['last_name']) : ''}
                            </p>
                            <p>
                                <span style={{fontWeight: 'bold'}}>Nacionalidade: </span>
                                {(playerInfo['nationality']) ? (playerInfo['nationality']) : ''}
                            </p>
                            <p>
                                <span style={{fontWeight: 'bold'}}>Idade: </span>
                                {(playerInfo['age'])? (playerInfo['age']) : ''}
                            </p>
                            <p>
                                <span style={{fontWeight: 'bold'}}>Data de nascimento: </span>
                                {(playerInfo['birth'])? (playerInfo['birth']['date'] ? playerInfo['birth']['date'] : 'N/A') : ''}
                            </p>
                            <p>
                                <span style={{fontWeight: 'bold'}}>Local de nascimento: </span>
                                {(playerInfo['birth'])? (playerInfo['birth']['place'] ? playerInfo['birth']['place'] : 'N/A') : ''}
                            </p>
                            <p>
                                <span style={{fontWeight: 'bold'}}>Altura: </span>
                                {(playerInfo['height'])? (playerInfo['height']) : ''}
                            </p>
                            <p>
                                <span style={{fontWeight: 'bold'}}>Peso: </span>
                                {(playerInfo['weight'])? (playerInfo['weight']) : ''}
                            </p>
                        </Paper>
                    </Grid>
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                            <Box sx={{height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                            </Box>
                        </Paper>
                    </Grid>
                </Grid>
            </PageContainer>
        </Paper>
    )
}

export default ExplorePlayer;