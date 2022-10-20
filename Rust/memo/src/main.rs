// -*- coding:utf-8-unix -*-
// #![feature(map_first_last)]
#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_macros)]
use core::num;
use std::any::Any;
use std::cmp::Ordering::*;
use std::collections::btree_map::Values;
use std::collections::*;
use std::convert::*;
use std::convert::{From, Into};
use std::error::Error;
use std::f32::consts::E;
use std::fmt::Debug;
use std::fmt::Display;
use std::fs::File;
use std::hash::Hash;
use std::io::prelude::*;
use std::io::*;
use std::iter::Filter;
use std::iter::FromIterator;
use std::marker::Copy;
use std::mem::*;
use std::ops::BitAnd;
use std::ops::Bound::*;
use std::ops::RangeBounds;
use std::ops::{Add, Mul, Neg, Sub};
use std::process;
use std::slice::from_raw_parts;
use std::str;
use std::vec;

const INF: i64 = 1223372036854775807;
const UINF: usize = INF as usize;
const LINF: i64 = 2147483647;
const INF128: i128 = 1223372036854775807000000000000;
// const MOD: i64 = 1000000007;
const MOD: i64 = 998244353;
const UMOD: usize = MOD as usize;
const M_PI: f64 = 3.14159265358979323846;
// const MOD: i64 = INF;

use std::cmp::*;
use std::collections::*;
use std::io::stdin;
use std::io::stdout;
use std::io::Write;

macro_rules! p {
    ($x:expr) => {
        println!("{}", $x);
    };
}

macro_rules! d {
    ($x:expr) => {
        println!("{:?}", $x);
    };
}

fn main() {
    solve();
}

// use str::Chars;
#[allow(dead_code)]
fn read<T: std::str::FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    s.trim().parse().ok().unwrap()
}

#[allow(dead_code)]
fn readi() -> (i64) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    iter.next().unwrap().parse::<i64>().unwrap()
}

#[allow(dead_code)]
fn read_vec<T: std::str::FromStr>() -> Vec<T> {
    read::<String>()
        .split_whitespace()
        .map(|e| e.parse().ok().unwrap())
        .collect()
}
#[allow(dead_code)]
fn read_mat<T: std::str::FromStr>(n: u32) -> Vec<Vec<T>> {
    (0..n).map(|_| read_vec()).collect()
}

#[allow(dead_code)]
fn readii() -> (i64, i64) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<i64>().unwrap(),
        iter.next().unwrap().parse::<i64>().unwrap(),
    )
}

#[allow(dead_code)]
fn readiii() -> (i64, i64, i64) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<i64>().unwrap(),
        iter.next().unwrap().parse::<i64>().unwrap(),
        iter.next().unwrap().parse::<i64>().unwrap(),
    )
}
#[allow(dead_code)]
fn readuu() -> (usize, usize) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<usize>().unwrap(),
        iter.next().unwrap().parse::<usize>().unwrap(),
    )
}

#[allow(dead_code)]
fn readff() -> (f64, f64) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<f64>().unwrap(),
        iter.next().unwrap().parse::<f64>().unwrap(),
    )
}

fn readcc() -> (char, char) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<char>().unwrap(),
        iter.next().unwrap().parse::<char>().unwrap(),
    )
}

fn readuuu() -> (usize, usize, usize) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<usize>().unwrap(),
        iter.next().unwrap().parse::<usize>().unwrap(),
        iter.next().unwrap().parse::<usize>().unwrap(),
    )
}
#[allow(dead_code)]
fn readiiii() -> (i64, i64, i64, i64) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<i64>().unwrap(),
        iter.next().unwrap().parse::<i64>().unwrap(),
        iter.next().unwrap().parse::<i64>().unwrap(),
        iter.next().unwrap().parse::<i64>().unwrap(),
    )
}

#[allow(dead_code)]
fn readuuuu() -> (usize, usize, usize, usize) {
    let mut str = String::new();
    let _ = stdin().read_line(&mut str).unwrap();
    let mut iter = str.split_whitespace();
    (
        iter.next().unwrap().parse::<usize>().unwrap(),
        iter.next().unwrap().parse::<usize>().unwrap(),
        iter.next().unwrap().parse::<usize>().unwrap(),
        iter.next().unwrap().parse::<usize>().unwrap(),
    )
}

fn solve() {
    let h = 10;
    let w = 10;
    let mut vv: Vec<Vec<char>> = vec![vec!['0' as char; (0) as usize]; (h) as usize];
    for i in 0..h {
        let s: String = read();
        let vvv = s.chars().collect();
        vv[i] = vvv;
    }
    let mut mih = UINF;
    let mut mah = 0;
    let mut miw = UINF;
    let mut maw = 0;
    for i in 0..10 {
        for j in 0..10 {
            if vv[i][j] == '#' {
                mih = min(mih, i);
                mah = max(mah, i);
                miw = min(miw, j);
                maw = max(maw, j);
            }
        }
    }
    println!("{} {}", mih + 1, mah + 1);
    println!("{} {}", miw + 1, maw + 1);
    return;
}
