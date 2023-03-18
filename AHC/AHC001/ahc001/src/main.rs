use std::{io::Write, time::Instant};
use std::fmt;
use rand::prelude::*;
use std::collections::BTreeSet;
 
const MAP_SIZE: u32 = 10000;
const MAP_DIV1: u32 = 5;
const MAP_EACH1: u32 = MAP_SIZE / MAP_DIV1;

macro_rules! chmin {
    ($val: expr, $new: expr) => {
        if $val > $new {
            $val = $new;
            true
        } else {
            false
        }
    };
}

macro_rules! chmax {
    ($val: expr, $new: expr) => {
        if $val < $new {
            $val = $new;
            true
        } else {
            false
        }
    };
}

#[derive(Copy, Clone, Debug)]

struct Request {
    row: u32,
    col: u32,
    area: u32
}

impl Request {
    fn new(row: u32, col: u32, area:u32) -> Self { Self { row, col, area } }

    fn rotate_right(&self) -> Self {
        Self::new(self.col, MAP_SIZE - self.row - 1, self.area)
    }
}


