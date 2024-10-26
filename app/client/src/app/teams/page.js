'use client'

import { useEffect, useState, Fragment } from 'react';
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import { getTeamsInfo } from '../api/team';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import Divider from '@mui/material/Divider';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import Link from 'next/link';

function getParams(teamsInfo, index) {
    return `teams/explore?name=${teamsInfo[index]?.name}&code=${teamsInfo[index]?.code}&logo=${teamsInfo[index]?.logo}`
}

function Teams() {
  const [teamsInfo, setTeamsInfo] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const dataTopStadiums = await getTeamsInfo()
      setTeamsInfo(dataTopStadiums)
    }
    fetchData()
  }, []);

  return (
    <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
      <PageContainer maxWidth="xl" sx={{marginBottom: '150px'}}>
        <Paper sx={{borderRadius: 3, p: 3}} elevation={3}>
            <Grid container >
                <Grid size={12}>
                        <List sx={{ width: '100%', overflow: 'auto' }}>
                            {teamsInfo ? teamsInfo.map((item, index) => (
                                <Box>
                                    <ListItemButton key={index} value={item} alignItems="flex-start" component={Link} to={getParams(teamsInfo, index)}>
                                        <ListItemAvatar>
                                            <Avatar alt="logo" src={teamsInfo[index]?.logo} />
                                        </ListItemAvatar>
                                        <ListItemText
                                            primary={teamsInfo[index]?.name}
                                            secondary={
                                                <Fragment>
                                                <Typography
                                                    component="span"
                                                    variant="body2"
                                                    sx={{ color: 'text.secondary', display: 'block' }}
                                                >
                                                    <span style={{fontWeight:'bold'}}>Sigla:</span> {teamsInfo[index]?.code}
                                                </Typography>
                                                <Typography
                                                    component="span"
                                                    variant="body2"
                                                    sx={{ color: 'text.secondary', display: 'block' }}
                                                >
                                                    <span style={{fontWeight:'bold'}}>Fundado:</span> {teamsInfo[index]?.founded}
                                                </Typography>
                                                <Typography
                                                    component="span"
                                                    variant="body2"
                                                    sx={{ color: 'text.secondary', display: 'block' }}
                                                >
                                                    <span style={{fontWeight:'bold'}}>País:</span> {teamsInfo[index]?.country}
                                                </Typography>                                            
                                                </Fragment>
                                            }
                                        />
                                    </ListItemButton>
                                    <Divider variant="inset" component="li" />
                                    </Box>
                            )) : ''}
                        </List>
                </Grid>
            </Grid>
        </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Teams;
