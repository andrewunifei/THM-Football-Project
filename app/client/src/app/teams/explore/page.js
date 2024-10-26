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
import GamesTable from '@/app/components/gamesTable';
import GoalsTable from '@/app/components/goalsTable';
import TeamGamesPieChart from '@/app/components/teamGamesPieChart';
import SegmentBarChart from '@/app/components/segmentBarChart';
import { getTeamsGamesInfo, getTeamsGoalsInfo } from '@/app/api/team';
import Divider from '@mui/material/Divider';
import GoalsPieChart from '@/app/components/goalsPizza';
import BiggestTable from '@/app/components/biggestTable';

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
            path: '/teams',
            title: 'Times'
        },
        {
            path: '',
            title: 'Explorar'
        }
    ]
}
  
function ExploreTeam() {
    const searchParams = useSearchParams();
    const code = searchParams.get('code')
    const name = searchParams.get('name')
    const logo = searchParams.get('logo')
    const [teamsGamesInfo, setTeamsGamesInfo] = useState([]);
    const [teamsGoalsInfo, setTeamsGoalsInfo] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
          const dataTeamGames = await getTeamsGamesInfo(code);
          const dataTeamGoals = await getTeamsGoalsInfo(code);
          setTeamsGamesInfo(dataTeamGames);
          setTeamsGoalsInfo(dataTeamGoals);
          console.log(teamsGoalsInfo)
        }
        fetchData();
    }, []);

    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}> 
            <PageContainer maxWidth="xl" breadcrumbs={getBread()} >
                {getTitle(logo, name)}
                <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Resultados</p>
                    <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                    <Grid container spacing={8} sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                        <Grid size={6} >
                            <Box>
                                <GamesTable teamsGamesInfo={teamsGamesInfo} />     
                            </Box>
                        </Grid>
                        <Grid size={6} sx={{height: 300}}>
                            <Box sx={{display: 'flex', alignItems: 'center', justifyContent: 'center', height: 300}}>
                                <TeamGamesPieChart teamsGamesInfo={teamsGamesInfo}/>
                            </Box>
                        </Grid>
                    </Grid>
                </Paper>
                <div style={{paddingTop:'25px'}}></div>
                <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                    <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Gols</p>
                    <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                    <Grid container spacing={8} sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                            <Grid size={6}>
                                <Grid container spacing={8} sx={{display: 'flex', flexDirection: 'column'}}>
                                    <Grid>
                                        <Box>
                                            <GoalsTable data={teamsGoalsInfo}/>
                                        </Box>
                                    </Grid>
                                    <Grid>
                                        <Box>
                                            <BiggestTable data={teamsGoalsInfo}/>
                                        </Box>
                                    </Grid>
                                </Grid>
                            </Grid>
                            <Grid size={6}>
                                <Box>
                                    <SegmentBarChart data={teamsGoalsInfo?.segments_for} data2={teamsGoalsInfo?.segments_against} />
                                </Box>
                                <Divider orientation="horizontal" style={{marginBottom: '20px', marginTop: '20px'}} />
                                <Grid container spacing={2}>
                                    <Grid size={4}>
                                        <GoalsPieChart 
                                            name='Jogos em casa'
                                            for_data={teamsGoalsInfo?.goals_for_home} 
                                            against_data={teamsGoalsInfo?.goals_against_home}
                                        />
                                    </Grid>
                                    <Grid size={4}>
                                        <GoalsPieChart 
                                            name='Jogos fora'
                                            for_data={teamsGoalsInfo?.goals_for_away}
                                            against_data={teamsGoalsInfo?.goals_against_away}
                                        />
                                    </Grid>
                                    <Grid size={4}>
                                        <GoalsPieChart 
                                            name='Total'
                                            for_data={teamsGoalsInfo?.goals_for_total}
                                            against_data={teamsGoalsInfo?.goals_against_total}
                                        />
                                </Grid>
                            </Grid> 
                        </Grid>
                    </Grid>
                </Paper>
                <div style={{paddingTop:'25px'}}></div>
                <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
                    <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>Cartões</p>
                    <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
                </Paper>
            </PageContainer>
        </Paper>
    )
}

export default ExploreTeam;