import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

export default function StadiumsMediaCard({ media=false }) {
  return (
    <Card sx={{ maxWidth: 345, maxHeight: 300 }}>
      <CardMedia
        sx={{ height: 140 }}
        image={media ? media['image'] : ''}
        title={media ? media['name'] : ''}
      />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {media ? media['name'] : ''}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }}>
              <span style={{fontWeight:'bold'}}>Capacidade:</span> {media ? media['capacity'].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") + ' pessoas' : ''} 
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }}>
              <span style={{fontWeight:'bold'}}>País:</span> {media ? media['country'] : ''}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }}>
              <span style={{fontWeight:'bold'}}>Cidade:</span> {media ? media['city'] : ''}
          </Typography>
            <Typography variant="body2" sx={{ color: 'text.secondary' }}>
              <span style={{fontWeight:'bold'}}>Endereço:</span> {media ? media['address'] : ''}
          </Typography>
        </CardContent>
    </Card>
  );
}
