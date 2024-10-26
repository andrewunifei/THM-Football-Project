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
import TeamGamesPieChart from '@/app/components/teamGamesPieChart';
import { getTeamsGamesInfo } from '@/app/api/team';

function PageToolbar() {
    return (
        <p>hello</p>
    );
}

function getTitle(logo, name) {
    return (
            <List sx={{ width: '100%', display: 'flex', alignItems:"flex-start" }}>
                <ListItem>
                    <ListItemAvatar>
                        <Avatar alt="logo" src={logo}/>
                    </ListItemAvatar>
                    {name}
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

    useEffect(() => {
        const fetchData = async () => {
          const dataTopStadiums = await getTeamsGamesInfo(code)
          setTeamsGamesInfo(dataTopStadiums)
        }
        fetchData()
    }, []);


    return (
        <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
        <PageContainer maxWidth="xl" slots={{toolbar: PageToolbar}} breadcrumbs={getBread()} title={getTitle(logo, name)}>
          <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
            <Grid container spacing={2} >
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                            <GamesTable teamsGamesInfo={teamsGamesInfo} />      
                    </Grid>
                    <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
                        <Box sx={{height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                            <TeamGamesPieChart teamsGamesInfo={teamsGamesInfo}/>
                        </Box>
                    </Grid>
                </Grid>
            </Paper>    
        </PageContainer>
      </Paper>
    )
}

export default ExploreTeam;