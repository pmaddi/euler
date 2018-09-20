use std::process;

fn approx_equal(a: f64, b: f64, decimal_places: u8) -> bool {
    let factor = 10.0f64.powi(decimal_places as i32);
    let a = (a * factor).trunc();
    let b = (b * factor).trunc();
    a == b
}

fn main() {
    let mut cnt = 0;
    let mut i = 1;
    loop {
        let mut j = 1;
        loop {
            let mut k = 1;
            loop {
                let x = (i * i) + (j + k) * (j + k);
                if approx_equal((x as f64).sqrt(), (x as f64).sqrt().trunc(), 10) {
                    cnt = cnt + 1;
                }
                if cnt > 1000000 {
                    println!("{} {}", i, cnt);
                    process::exit(1);
                }
                k = k + 1;
                if k > j {break;}
            }
            j = j + 1;
            if j > i {break;}
        }
        i = i + 1;
    }
}

