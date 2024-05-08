import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';

class Row {
    constructor(id_, perf_, infrstr_, curm_, emplt_ = null, sci_ = null, intnat_ = null){
        this.id = id_;
        this.perf = perf_;
        this.infrstr = infrstr_;
        this.curm = curm_;
        this.emplt = emplt_;
        this.sci = sci_;
        this.intnat = intnat_;
    }

    get items(){
        return this.id, this.perf, this.infrstr, this.curm, this.emplt, this.sci, this.intnat;
    }
};

const rows = [
  new Row("R.E.Alexeev NNSTU", 7, 7, 7)
];

function preventDefault(event) {
  event.preventDefault();
}

export default function UnivRating() {
  return (
    <React.Fragment>
      <Toolbar>
            <Typography
              component="h1"
              variant="h6"
              color="inherit"
              noWrap
              sx={{ flexGrow: 1 }}
            >
              Dashboard
            </Typography>
          </Toolbar>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Ship To</TableCell>
            <TableCell>Payment Method</TableCell>
            <TableCell align="right">Sale Amount</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
              <TableCell>{row.paymentMethod}</TableCell>
              <TableCell align="right">{`$${row.amount}`}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}