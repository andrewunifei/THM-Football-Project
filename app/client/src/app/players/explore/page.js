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
import { getPlayerInfo, getPlayerInjuries, getPlayerHistoric } from '@/app/api/player';
import PlayersInjuriesTable from '@/app/components/players/playersInjuriesTable';

function getTitle(logo, name, teamLogo, teamName) {
    return (
        <Grid container spacing={0} sx={{
            width: '100%',
            display: 'flex',
            justifyContent:"space-between",
            alignItems:"center",
            marginBottom: '20px'
        }} >
            <Grid sx={{display: 'flex', alignItems:"center"}}>
                <ListItemAvatar>
                    <Avatar alt="logo" src={logo}/>
                </ListItemAvatar>
                <p style={{fontSize: '34px', font: 'roboto', fontWeight: '100'}}>{name}</p>
            </Grid>
            <Grid sx={{display: 'flex', alignItems:"center", justifyContent:"center", flexDirection:"column"}}>
                <Avatar alt="logo" src={teamLogo} />
                <p>{teamName}</p>
            </Grid>
        </Grid>
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
    const [ playerInjuries, setPlayerInjuries ] = useState({})
    const [ playerHistoric, setPlayerHistoric ] = useState({})
    const searchParams = useSearchParams();
    const playerId = searchParams.get('player-id')
    const name = searchParams.get('name')
    const photo = searchParams.get('photo')
    const teamLogo = searchParams.get('team-logo')
    const teamName = searchParams.get('team-name')

    useEffect(() => {
        const fetchData = async () => {
            const playerData = await getPlayerInfo(playerId)
            const injuriesData = await getPlayerInjuries(playerId)
            const historicData = await getPlayerHistoric(playerId)
            setPlayerInfo(playerData)
            setPlayerInjuries(injuriesData)
            setPlayerHistoric(historicData)
          }
          fetchData();
    }, [])

    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}> 
            <PageContainer maxWidth="xl" breadcrumbs={getBread()} sx={{marginBottom: '150px'}}>
                {playerInfo['player_id'] ?
                (
                    <>
                    <Grid container spacing={3} >
                        <Grid size={6}>
                            <Paper sx={{borderRadius: 3, p: 5, height: 370}} elevation={3}>
                                {getTitle(photo, name, teamLogo, teamName)}
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
                            <Paper sx={{borderRadius: 3, p: 5, height: 370}} elevation={3}>
                                <div style={{width: '100%'}}>
                                <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100', display: 'flex', justifyContent:"center", alignItems:"center"}}>Estatísticas na Liga</p>
                                </div>
                                <Divider orientation="horizontal" style={{marginBottom: '20px', marginTop: '20px'}} />
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
                                                    <p><span style={{fontWeight: 'bold'}}>Lesões: </span>{playerInjuries.data.length}</p>
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
                    {(playerInjuries.data.length > 0) ?
                        <>
                        <div style={{paddingTop:'25px'}}></div>
                        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                            <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Lesões</p>
                            <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                            <Grid container sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                                <Grid size={12} >
                                    <Box>
                                        <PlayersInjuriesTable playerInjuries={playerInjuries}/>
                                    </Box>
                                </Grid>
                            </Grid>
                        </Paper>
                        </>
                    : ''}
                    <div style={{paddingTop:'25px'}}></div>
                    <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                        <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Jogos</p>
                        <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                        <Grid container spacing={8} sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                            <Grid size={6} >
                                <Box>
                                </Box>
                            </Grid>
                            <Grid size={6} sx={{height: 300}}>
                                <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', height: 300}}>
                                </Box>
                            </Grid>
                        </Grid>
                    </Paper>
                    <div style={{paddingTop:'25px'}}></div>
                    <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                        <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Histórico de Times</p>
                        <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                        <Grid container spacing={8} sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                            <Grid size={6} >
                                <Box>
                                </Box>
                            </Grid>
                            <Grid size={6} sx={{height: 300}}>
                                <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', height: 300}}>

                                </Box>
                            </Grid>
                        </Grid>
                    </Paper>
                    </>
                ) : '' }
            </PageContainer>
        </Paper>
    )
}

export default ExplorePlayer;