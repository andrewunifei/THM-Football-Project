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

                        </Paper>
                    </Grid>
                </Grid>
            </PageContainer>
        </Paper>
    )
}

export default ExploreGame;