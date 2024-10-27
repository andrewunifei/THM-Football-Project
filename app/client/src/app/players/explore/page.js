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
                {playerInfo['player_id'] ?
                (
                    <Grid container spacing={3} >
                        <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                            <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                                <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Identificação Geral</p>
                                <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Nome completo: </span>
                                    {(playerInfo['first_name'] && playerInfo['last_name']) ? (playerInfo['first_name'] + ' ' + playerInfo['last_name']) : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Nacionalidade: </span>
                                    {(playerInfo['nationality']) ? playerInfo['nationality'] : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Idade: </span>
                                    {(playerInfo['age']) ? playerInfo['age'] : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Data de nascimento: </span>
                                    {(playerInfo['birth']) ? (playerInfo['birth']['date'] ? playerInfo['birth']['date'] : 'N/A') : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Local de nascimento: </span>
                                    {(playerInfo['birth']) ? (playerInfo['birth']['place'] ? playerInfo['birth']['place'] : 'N/A') : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Altura: </span>
                                    {(playerInfo['height']) ? playerInfo['height'] : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Peso: </span>
                                    {(playerInfo['weight']) ? playerInfo['weight'] : 'N/A'}
                                </p>
                                <p>
                                    <span style={{fontWeight: 'bold'}}>Posição: </span>
                                    {(playerInfo['position']) ? playerInfo['position'] : 'N/A'}
                                </p>
                            </Paper>
                        </Grid>
                        <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                            <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                                <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Estatísticas na Liga</p>
                                <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                                    {
                                        playerInfo['games_appearences'] ?
                                            (
                                                <>
                                                    <p><span style={{fontWeight: 'bold'}}>Jogos jogados: </span>{playerInfo['games_appearences']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Minutos jogados: </span>{playerInfo['minutes_played_total'] == null ? 'N/A' : playerInfo['minutes_played_total']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Gols: </span>{playerInfo['goals_total'] == null ? 'N/A' : playerInfo['goals_total']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Passes: </span>{playerInfo['passes_total'] == null ? 'N/A' : playerInfo['passes_total']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Passes chaves: </span>{playerInfo['passes_key'] == null ? 'N/A' : playerInfo['passes_key']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Cartões amarelos: </span>{playerInfo['cards_yellow_total'] == null ? 'N/A' : playerInfo['cards_yellow_total']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Cartões vermelhos: </span>{playerInfo['cards_red_total'] == null ? 'N/A' : playerInfo['cards_red_total']}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Nota: </span>{playerInfo['rating'].slice(0,4)}</p>
                                                </>
                                            )
                                            : (playerInfo['games_appearences'] == 0 ) ?
                                                (<p><span style={{fontWeight: 'bold'}}>Jogos jogados: </span>0</p>) 
                                                : (<p><span style={{fontWeight: 'bold'}}>Jogos jogados: </span>N/A</p>)
                                    }
                            </Paper>
                        </Grid>
                    </Grid>
                ) : '' }
            </PageContainer>
        </Paper>
    )
}

export default ExplorePlayer;