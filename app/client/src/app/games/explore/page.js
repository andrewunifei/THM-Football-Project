'use client'

import { useState, useEffect } from 'react';
import { useSearchParams } from 'next/navigation'
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Avatar from '@mui/material/Avatar';
import Divider from '@mui/material/Divider';
import { getGameDetails } from '@/app/api/game';

function getTitle(logo, name) {
    return (
        <>
            
        </>
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
    const [gameDetails, setGameDetails] = useState([])
    const searchParams = useSearchParams();
    const game_id = searchParams.get('game-id')

    useEffect(() => {
        const fetchdata = async () => {
            const data = await getGameDetails(game_id)
            setGameDetails(data)
        }
        fetchdata()
    }, [])

    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}> 
            <PageContainer maxWidth="xl" breadcrumbs={getBread()} sx={{marginBottom: '150px'}} >
                <Grid container spacing={3} >
                    <Grid size={6}>
                        <Paper elevation={3} sx={{borderRadius: 3, paddingTop: 3, paddingBottom: 3, height: 370, display: 'flex', justifyContent: 'center', alignContent:'center',  flexDirection:'column'}}>
                            <Divider/>
                            <Box sx={{borderRadius: 3, p: 5, display: 'flex', justifyContent: 'center', alignContent:'center',  flexDirection:'column'}}>
                            {gameDetails ? (
                                <Grid container spacing={0} direction={'row'}>
                                    <Grid size={5}>
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <Avatar alt="logo" src={gameDetails?.home_logo} sx={{ width: 120, height: 120 }}/>
                                        </Box>
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <p style={{fontSize: '20px', font: 'roboto', fontWeight: '100'}}>{gameDetails?.home_name}</p>  
                                        </Box>
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <p style={{fontSize: '30px', font: 'roboto', fontWeight: '100'}}>{gameDetails.game?.home_team_goals}</p>  
                                        </Box>
                                    </Grid>
                                    <Grid size={2} sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'column'}}>
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <span style={{fontSize: '36px', font: 'roboto', fontWeight: '100', fontStyle: 'italic'}}>VS</span> 
                                        </Box>
                                    </Grid>
                                    <Grid size={5}>
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <Avatar alt="logo" src={gameDetails?.away_logo} sx={{ width: 120, height: 120 }} />
                                        </Box>
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <p style={{fontSize: '20px', font: 'roboto', fontWeight: '100'}}>{gameDetails?.away_name}</p>  
                                        </Box>  
                                        <Box sx={{display: 'flex', justifyContent: 'center', alignContent:'center', flexDirection:'row'}}>
                                            <p style={{fontSize: '30px', font: 'roboto', fontWeight: '100'}}>{gameDetails?.game?.away_team_goals}</p>  
                                        </Box>
                                    </Grid>
                                </Grid>
                            ): ''}
                            </Box>
                            <Divider/>
                        </Paper>
                    </Grid>
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                        <Paper sx={{borderRadius: 3, p: 5, height: 370}} elevation={3}>
                        <div style={{width: '100%'}}>
                                <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100', display: 'flex', justifyContent:"center", alignItems:"center"}}>Informações da Partida</p>
                                </div>
                                <Divider orientation="horizontal" style={{marginBottom: '20px', marginTop: '20px'}} />
                                    {
                                        gameDetails ?
                                            (
                                                <>
                                                    <p><span style={{fontWeight: 'bold'}}>Data: </span>{gameDetails?.game?.date}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Árbitro: </span>{gameDetails?.game?.referee}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Time casa: </span>{gameDetails?.home_name}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Time fora: </span>{gameDetails?.away_name}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Estádio: </span>{gameDetails?.stadium_name}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Capacidade estádio: </span>{gameDetails?.stadium_capacity?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")} pessoas</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Endereço: </span>{gameDetails?.stadium_address}</p>
                                                    <p><span style={{fontWeight: 'bold'}}>Cidade: </span>{gameDetails?.city}</p>
                                                </>
                                            ) : ''
                                    }
                        </Paper>
                    </Grid>
                </Grid>
                <div style={{paddingTop:'25px'}}></div>
                    <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                        <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Estatísticas {gameDetails?.home_name} (Time Casa)</p>
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
                        <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Estatísticas {gameDetails?.away_name} (Time Fora)</p>
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
            </PageContainer>
        </Paper>
    )
}

export default ExploreGame;