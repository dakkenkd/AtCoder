use std::collections::{HashSet, VecDeque};
use proconio::input;

fn main() {
    input!{
        n: usize, m: usize,
        mut e: [(usize, usize); m],
    };

    let mut g: Vec<Vec<usize>> = vec![vec![]; n+1];
    let mut set: HashSet<(usize, usize)> = HashSet::new();
    for &(u, v) in &e {
        g[u].push(v);
        set.insert((u, v));
    }

    let mut res = 0;

    for s in 1..=n {
        let mut q: VecDeque<usize> = VecDeque::new();
        let mut seen: Vec<bool> = vec![false; n+1];
        q.push_back(s);
        seen[s] = true;
        while q.len() > 0 {
            let u = q.pop_front().unwrap();
            for &v in &g[u] {
                if seen[v] {continue;}
                res += 1
                q.push_back(v);
                seen[v] = true;
            }
        }
    }
    println!("{}", res-m);
}
