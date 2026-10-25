import json
from pathlib import Path
questions=[]
def add(ch,code,topic,te,ti,pe,pi,se,si,visual=None):
 band={'C':'Core','H':'Challenge','A':'Advanced'}[code[0]];n=int(code[1:])
 if ch==1: qp=1 if code[0]=='C' else (2 if code[0]=='H' or code=='A1' else 3);sp=4 if code[0]=='C' or code in ['H1','H2'] else (5 if code[0]=='H' or code in ['A1','A2'] else 6)
 elif ch==2: qp=1 if code[0]=='C' else (2 if code[0]=='H' or (code[0]=='A' and n<=4) else 3);sp=4 if code[0]=='C' or (code[0]=='H' and n<=3) else (5 if code[0]=='H' or n<=5 else 6)
 else: qp=1 if code[0]=='C' or (code[0]=='H' and n<=4) else (2 if code[0]=='H' else 3);sp=4 if code[0]=='C' or (code[0]=='H' and n<=6) else (5 if code[0]=='H' else 6)
 questions.append(dict(id=f'FG{ch}-{code}',chapter=ch,code=code,level=band,topic=topic,title=dict(en=te,id=ti),prompt=dict(en=pe,id=pi),steps=dict(en=se,id=si),source=dict(questionPage=qp,solutionPage=sp),visual=visual))
add(1,'C1','meaning','Function or not?','Fungsi atau bukan?',
'Relation A: −2 ↦ 1, 0 ↦ 1, 3 ↦ 5.\nRelation B: 1 ↦ 2, 1 ↦ 4, 3 ↦ 6.\n(a) Which relation is a function? (b) Is A one-to-one or many-to-one? (c) Why does B fail?',
'Relasi A: −2 ↦ 1, 0 ↦ 1, 3 ↦ 5.\nRelasi B: 1 ↦ 2, 1 ↦ 4, 3 ↦ 6.\n(a) Relasi mana yang merupakan fungsi? (b) Apakah A satu-ke-satu atau banyak-ke-satu? (c) Mengapa B bukan fungsi?',
['A is a function: each input has exactly one output.','A is many-to-one: −2 and 0 share output 1.','B is not a function: input 1 has two distinct outputs, 2 and 4.'],
['A adalah fungsi: setiap input mempunyai tepat satu output.','A banyak-ke-satu: −2 dan 0 sama-sama menghasilkan 1.','B bukan fungsi: input 1 menghasilkan dua output berbeda, 2 dan 4.'],'mapping')
add(1,'C2','notation','Function notation','Notasi fungsi',
'Let f(x)=2x²−3x+1. Find (a) f(−2), (b) f(a), (c) f(x+1).',
'Diberikan f(x)=2x²−3x+1. Tentukan (a) f(−2), (b) f(a), (c) f(x+1).',
['f(−2)=2(−2)²−3(−2)+1=8+6+1=15.','f(a)=2a²−3a+1.','f(x+1)=2(x+1)²−3(x+1)+1=2x²+x.'],
['f(−2)=2(−2)²−3(−2)+1=8+6+1=15.','f(a)=2a²−3a+1.','f(x+1)=2(x+1)²−3(x+1)+1=2x²+x.'])
add(1,'C3','notation','Find the input','Mencari input',
'Let g(x)=4x−7 and g(a)=21. Find a.','Diberikan g(x)=4x−7 dan g(a)=21. Tentukan a.',
['Substitute the input a: 4a−7=21.','4a=28, so a=7.','Check: g(7)=28−7=21.'],['Substitusi input a: 4a−7=21.','4a=28, sehingga a=7.','Cek: g(7)=28−7=21.'])
add(1,'C4','domain','Domain restrictions','Pembatasan domain',
'State the real domain of (a) f(x)=5/(x−2), (b) g(x)=√(2x+6), (c) h(x)=x³−4x+1. Explain each restriction.',
'Tentukan domain real (a) f(x)=5/(x−2), (b) g(x)=√(2x+6), (c) h(x)=x³−4x+1. Jelaskan tiap pembatasan.',
['(a) The denominator must be nonzero: x≠2; D=ℝ∖{2}.','(b) The radicand must be nonnegative: 2x+6≥0 → x≥−3; D=[−3,∞).','(c) A polynomial is defined for every real input; D=ℝ.'],
['(a) Penyebut tidak boleh nol: x≠2; D=ℝ∖{2}.','(b) Bentuk di dalam akar harus nonnegatif: 2x+6≥0 → x≥−3; D=[−3,∞).','(c) Polinom terdefinisi untuk setiap input real; D=ℝ.'])
add(1,'C5','domain','Range on a restricted domain','Range pada domain terbatas',
'Let f(x)=x²+1 with −2≤x≤3. Find the range.','Diberikan f(x)=x²+1 dengan −2≤x≤3. Tentukan range.',
['The minimum occurs at x=0, which is in the domain: f(0)=1.','Check both endpoints: f(−2)=5 and f(3)=10.','The continuous function attains every value between its minimum and maximum: R=[1,10].'],
['Minimum terjadi pada x=0 yang termasuk domain: f(0)=1.','Periksa kedua ujung: f(−2)=5 dan f(3)=10.','Fungsi kontinu mengambil semua nilai antara minimum dan maksimum: R=[1,10].'],'restricted-square')
add(1,'C6','meaning','Domain, range and one-to-one','Domain, range, dan satu-ke-satu',
'A relation consists of (−2,3), (0,1), (4,3), (5,6). Find its domain and range; decide whether it is a function and whether it is one-to-one.',
'Suatu relasi terdiri atas (−2,3), (0,1), (4,3), (5,6). Tentukan domain dan range; putuskan apakah relasi ini fungsi dan satu-ke-satu.',
['The distinct inputs give D={−2,0,4,5}.','The distinct outputs give R={1,3,6}.','It is a function, but not one-to-one: −2 and 4 both map to 3.'],
['Input berbeda memberikan D={−2,0,4,5}.','Output berbeda memberikan R={1,3,6}.','Relasi ini fungsi, tetapi bukan satu-ke-satu: −2 dan 4 sama-sama dipetakan ke 3.'])
add(1,'C7','inverse','Which function is one-to-one?','Fungsi mana yang satu-ke-satu?',
'Compare f(x)=3x−2 and g(x)=x² on ℝ. Which is one-to-one? Justify, and give two different inputs showing why the other is not.',
'Bandingkan f(x)=3x−2 dan g(x)=x² pada ℝ. Mana yang satu-ke-satu? Jelaskan dan berikan dua input berbeda yang menunjukkan mengapa fungsi lainnya tidak.',
['If f(a)=f(b), then 3a−2=3b−2, so a=b; f is one-to-one.','g(2)=g(−2)=4, although 2≠−2.','Therefore g is many-to-one on ℝ and has no inverse function on that full domain.'],
['Jika f(a)=f(b), maka 3a−2=3b−2 sehingga a=b; f satu-ke-satu.','g(2)=g(−2)=4, padahal 2≠−2.','Jadi g banyak-ke-satu pada ℝ dan tidak mempunyai fungsi invers pada seluruh domain itu.'])
add(1,'C8','composition','Composition order','Urutan komposisi',
'Let f(x)=2x+1 and g(x)=x². Find fg(x) and gf(x). Hence explain why fg≠gf. Here fg(x)=f(g(x)).',
'Diberikan f(x)=2x+1 dan g(x)=x². Tentukan fg(x) dan gf(x), lalu jelaskan mengapa fg≠gf. Notasi fg(x)=f(g(x)).',
['fg(x)=f(x²)=2x²+1.','gf(x)=g(2x+1)=(2x+1)².','These expressions differ; for example fg(1)=3 while gf(1)=9.'],
['fg(x)=f(x²)=2x²+1.','gf(x)=g(2x+1)=(2x+1)².','Kedua bentuk berbeda; misalnya fg(1)=3 sedangkan gf(1)=9.'])
add(1,'C9','inverse','Simple inverse','Invers sederhana',
'Let f(x)=5x−4. (a) Find f⁻¹(x). (b) Find f⁻¹(11). (c) Interpret the result in terms of f.',
'Diberikan f(x)=5x−4. (a) Tentukan f⁻¹(x). (b) Hitung f⁻¹(11). (c) Tafsirkan hasilnya dalam f.',
['Write y=5x−4 and solve for the input: x=(y+4)/5.','Swap names: f⁻¹(x)=(x+4)/5. Thus f⁻¹(11)=15/5=3.','This means f(3)=11: the inverse recovers the input that produced 11.'],
['Tulis y=5x−4 dan cari input: x=(y+4)/5.','Tukar nama: f⁻¹(x)=(x+4)/5. Maka f⁻¹(11)=15/5=3.','Artinya f(3)=11: invers mengembalikan input yang menghasilkan 11.'])
add(1,'C10','transform','Track a point','Lacak sebuah titik',
'The point (−1,4) lies on y=f(x). Find its corresponding point on (a) y=f(x−3)+2, (b) y=−f(x).',
'Titik (−1,4) terletak pada y=f(x). Tentukan bayangannya pada (a) y=f(x−3)+2, (b) y=−f(x).',
['For f(x−3)+2, (a,b) maps to (a+3,b+2).','Thus (−1,4) maps to (2,6).','For −f(x), (a,b) maps to (a,−b), giving (−1,−4).'],
['Untuk f(x−3)+2, (a,b) dipetakan ke (a+3,b+2).','Jadi (−1,4) menjadi (2,6).','Untuk −f(x), (a,b) menjadi (a,−b), sehingga diperoleh (−1,−4).'],'point-transform')
add(1,'H1','domain','Read a graph description','Baca deskripsi grafik',
'A continuous graph begins at an open point (−3,5), falls to a closed minimum (1,−2), then rises to a closed endpoint (4,3). Everywhere else it stays below y=5. Determine domain and range.',
'Grafik kontinu dimulai pada titik terbuka (−3,5), turun ke minimum tertutup (1,−2), lalu naik ke ujung tertutup (4,3). Di tempat lain grafik berada di bawah y=5. Tentukan domain dan range.',
['The x-values extend from −3 excluded to 4 included: D=(−3,4].','The minimum output −2 is attained. Output 5 occurs only at the excluded left endpoint.','Continuity fills the intervening outputs, so R=[−2,5).'],
['Nilai x membentang dari −3 yang dikeluarkan sampai 4 yang disertakan: D=(−3,4].','Output minimum −2 dicapai. Output 5 hanya ada pada ujung kiri yang dikeluarkan.','Kontinuitas mengisi output di antaranya, sehingga R=[−2,5).'],'described-graph')
add(1,'H2','composition','Same functions, different order','Fungsi sama, urutan berbeda',
'Let f(x)=x−1 and g(x)=√(5−x). Find fg(x) and its domain, then gf(x) and its domain. Explain why the domains differ.',
'Diberikan f(x)=x−1 dan g(x)=√(5−x). Tentukan fg(x) beserta domainnya, lalu gf(x) beserta domainnya. Jelaskan perbedaannya.',
['fg(x)=f(√(5−x))=√(5−x)−1, requiring 5−x≥0, so x≤5.','gf(x)=g(x−1)=√(5−(x−1))=√(6−x), requiring x≤6.','The order changes the expression entering the square root, hence the domain.'],
['fg(x)=f(√(5−x))=√(5−x)−1; syarat 5−x≥0 memberi x≤5.','gf(x)=g(x−1)=√(5−(x−1))=√(6−x); syaratnya x≤6.','Urutan mengubah bentuk yang masuk ke akar, sehingga domain berubah.'])
add(1,'H3','inverse','Rational inverse','Invers rasional',
'Let f(x)=(2x+3)/(x−1). State the domain, find f⁻¹(x), determine the range of f, then give the domain and range of f⁻¹.',
'Diberikan f(x)=(2x+3)/(x−1). Tentukan domain, f⁻¹(x), range f, serta domain dan range f⁻¹.',
['D_f=ℝ∖{1}. From y(x−1)=2x+3, obtain x(y−2)=y+3.','Thus f⁻¹(x)=(x+3)/(x−2). Output 2 is impossible for f.','R_f=D_(f⁻¹)=ℝ∖{2}; R_(f⁻¹)=ℝ∖{1}.'],
['D_f=ℝ∖{1}. Dari y(x−1)=2x+3, diperoleh x(y−2)=y+3.','Jadi f⁻¹(x)=(x+3)/(x−2). Output 2 tidak mungkin dihasilkan f.','R_f=D_(f⁻¹)=ℝ∖{2}; R_(f⁻¹)=ℝ∖{1}.'])
add(1,'H4','inverse','Restricted quadratic inverse','Invers kuadrat terbatas',
'Let f(x)=(x+1)²−4 with x≤−1. (a) Explain why f is one-to-one. (b) Find its range. (c) Find f⁻¹(x). (d) State the inverse domain and range.',
'Diberikan f(x)=(x+1)²−4 dengan x≤−1. (a) Mengapa f satu-ke-satu? (b) Tentukan range. (c) Tentukan f⁻¹(x). (d) Nyatakan domain dan range invers.',
['The restriction retains the strictly decreasing left branch, so f is one-to-one. Its vertex is (−1,−4), giving R_f=[−4,∞).','From y+4=(x+1)² and x+1≤0, use x+1=−√(y+4).','f⁻¹(x)=−1−√(x+4); D_(f⁻¹)=[−4,∞), R_(f⁻¹)=(−∞,−1].'],
['Pembatasan menyisakan cabang kiri yang turun tegas, sehingga f satu-ke-satu. Puncaknya (−1,−4), maka R_f=[−4,∞).','Dari y+4=(x+1)² dan x+1≤0, gunakan x+1=−√(y+4).','f⁻¹(x)=−1−√(x+4); D_(f⁻¹)=[−4,∞), R_(f⁻¹)=(−∞,−1].'],'quadratic-inverse')
add(1,'H5','inverse','Verify an inverse','Verifikasi invers',
'Let f(x)=3x−4. A student claims g(x)=(x+4)/3 is f⁻¹. Verify using both fg(x) and gf(x).',
'Diberikan f(x)=3x−4. Seorang siswa menyatakan g(x)=(x+4)/3 adalah f⁻¹. Verifikasi melalui fg(x) dan gf(x).',
['fg(x)=3((x+4)/3)−4=x.','gf(x)=((3x−4)+4)/3=x.','Both compositions are the identity on ℝ, so g=f⁻¹.'],
['fg(x)=3((x+4)/3)−4=x.','gf(x)=((3x−4)+4)/3=x.','Kedua komposisi adalah identitas pada ℝ, sehingga g=f⁻¹.'])
add(1,'H6','transform','Reconstruct a transformation','Rekonstruksi transformasi',
'P=(1,3) and Q=(4,−1) on y=f(x) become P′=(5,8) and Q′=(8,0) under y=2f(x−h)+k. Find h, k and the transformed equation.',
'P=(1,3) dan Q=(4,−1) pada y=f(x) menjadi P′=(5,8) dan Q′=(8,0) oleh y=2f(x−h)+k. Tentukan h, k, dan persamaan transformasinya.',
['Input coordinates shift by h: 1+h=5 and 4+h=8, so h=4.','From P: 2(3)+k=8 → k=2. Check Q: 2(−1)+2=0.','The equation is y=2f(x−4)+2.'],
['Koordinat input bergeser h: 1+h=5 dan 4+h=8, maka h=4.','Dari P: 2(3)+k=8 → k=2. Cek Q: 2(−1)+2=0.','Persamaannya y=2f(x−4)+2.'])
add(1,'H7','transform','Absolute value transformation','Transformasi nilai mutlak',
'The graph y=f(x) crosses at x=−1 and x=3, lies below the axis for −1<x<3, and contains (0,−4) and (4,2). For y=|f(x)|, determine the intercepts, images of both points, and which part reflects.',
'Grafik y=f(x) melintas pada x=−1 dan x=3, di bawah sumbu untuk −1<x<3, serta melalui (0,−4) dan (4,2). Untuk y=|f(x)|, tentukan intersep, bayangan kedua titik, dan bagian yang direfleksikan.',
['Zeros remain zeros, so the x-intercepts stay (−1,0) and (3,0).','(0,−4) maps to (0,4), so the new y-intercept is (0,4); (4,2) stays fixed.','The part below the x-axis, −1<x<3, reflects upward across that axis.'],
['Nilai nol tetap nol, sehingga intersep-x tetap (−1,0) dan (3,0).','(0,−4) menjadi (0,4), jadi intersep-y baru (0,4); (4,2) tetap.','Bagian di bawah sumbu-x, −1<x<3, direfleksikan ke atas terhadap sumbu tersebut.'])
add(1,'H8','composition','Find a missing function','Mencari fungsi yang hilang',
'Let f(x)=x+4 and gf(x)=2x+1. Find g(x).','Diberikan f(x)=x+4 dan gf(x)=2x+1. Tentukan g(x).',
['g(x+4)=2x+1. Set u=x+4, so x=u−4.','g(u)=2(u−4)+1=2u−7, hence g(x)=2x−7.','Check: g(f(x))=2(x+4)−7=2x+1.'],
['g(x+4)=2x+1. Ambil u=x+4 sehingga x=u−4.','g(u)=2(u−4)+1=2u−7, jadi g(x)=2x−7.','Cek: g(f(x))=2(x+4)−7=2x+1.'])
add(1,'H9','inverse','Invert a mapping','Membalik pemetaan',
'A one-to-one function maps −2 ↦ 5, 0 ↦ 1, 3 ↦ 7. Write the inverse mapping, its domain and its range.',
'Fungsi satu-ke-satu memetakan −2 ↦ 5, 0 ↦ 1, 3 ↦ 7. Tulis pemetaan invers beserta domain dan range-nya.',
['Reverse each arrow: 5 ↦ −2, 1 ↦ 0, 7 ↦ 3.','The inverse domain is the original range: {1,5,7}.','The inverse range is the original domain: {−2,0,3}.'],
['Balik tiap panah: 5 ↦ −2, 1 ↦ 0, 7 ↦ 3.','Domain invers adalah range asal: {1,5,7}.','Range invers adalah domain asal: {−2,0,3}.'])
add(1,'H10','domain','Find a domain restriction','Mencari pembatasan domain',
'Let f(x)=(x−1)² with x≥k, where k≥1. Its range is y≥9. Find k and explain why k≥1 matters.',
'Diberikan f(x)=(x−1)² dengan x≥k, k≥1. Range-nya y≥9. Tentukan k dan jelaskan pentingnya k≥1.',
['On x≥k≥1 the quadratic is increasing, so the minimum output is (k−1)².','Set (k−1)²=9 → k=4 or −2.','Only k=4 satisfies k≥1. That condition keeps the domain on the increasing branch.'],
['Pada x≥k≥1, kuadrat naik sehingga minimum output adalah (k−1)².','Ambil (k−1)²=9 → k=4 atau −2.','Hanya k=4 memenuhi k≥1. Syarat itu menjaga domain pada cabang naik.'])
add(1,'A1','composition','Recover a function from a composite','Memulihkan fungsi dari komposisi',
'Let g(x)=√(x+1). For x≥−4, gf(x)=x+4. Find f(x) on this domain and verify the composition is valid.',
'Diberikan g(x)=√(x+1). Untuk x≥−4, gf(x)=x+4. Tentukan f(x) pada domain ini dan verifikasi keabsahan komposisinya.',
['√(f(x)+1)=x+4, whose right side is nonnegative on x≥−4.','Squaring gives f(x)+1=(x+4)², so f(x)=x²+8x+15.','f(x)+1=(x+4)²≥0 and √((x+4)²)=|x+4|=x+4 on the stated domain.'],
['√(f(x)+1)=x+4; ruas kanan nonnegatif pada x≥−4.','Kuadratkan: f(x)+1=(x+4)², sehingga f(x)=x²+8x+15.','f(x)+1=(x+4)²≥0 dan √((x+4)²)=|x+4|=x+4 pada domain tersebut.'])
add(1,'A2','composition','Composition and inverse','Komposisi dan invers',
'Let f(x)=3x−1 and g(x)=1/(x+2). Find fg(x), its domain, (fg)⁻¹(x), and the inverse domain/range. Verify one inverse composition.',
'Diberikan f(x)=3x−1 dan g(x)=1/(x+2). Tentukan fg(x), domainnya, (fg)⁻¹(x), serta domain/range invers. Verifikasi satu komposisi invers.',
['F(x)=fg(x)=3/(x+2)−1=(1−x)/(x+2), x≠−2.','y(x+2)=1−x → x(y+1)=1−2y, so F⁻¹(x)=(1−2x)/(x+1).','D_(F⁻¹)=ℝ∖{−1}; R_(F⁻¹)=ℝ∖{−2}.','For x≠−2, F(x)+1=3/(x+2) and 1−2F(x)=3x/(x+2), so F⁻¹(F(x))=x.'],
['F(x)=fg(x)=3/(x+2)−1=(1−x)/(x+2), x≠−2.','y(x+2)=1−x → x(y+1)=1−2y, jadi F⁻¹(x)=(1−2x)/(x+1).','D_(F⁻¹)=ℝ∖{−1}; R_(F⁻¹)=ℝ∖{−2}.','Untuk x≠−2, F(x)+1=3/(x+2) dan 1−2F(x)=3x/(x+2), sehingga F⁻¹(F(x))=x.'])
add(1,'A3','inverse','Parameter from inverse domain','Parameter dari domain invers',
'Let f(x)=(x−2)²+k, x≥2. The domain of f⁻¹ is x≥5. Find k, f⁻¹(x), and its range.',
'Diberikan f(x)=(x−2)²+k, x≥2. Domain f⁻¹ adalah x≥5. Tentukan k, f⁻¹(x), dan range invers.',
['On the right branch, R_f=[k,∞), which equals the inverse domain [5,∞), so k=5.','From y−5=(x−2)² and x−2≥0, obtain x=2+√(y−5).','f⁻¹(x)=2+√(x−5), x≥5; its range is y≥2.'],
['Pada cabang kanan, R_f=[k,∞), sama dengan domain invers [5,∞), sehingga k=5.','Dari y−5=(x−2)² dan x−2≥0, diperoleh x=2+√(y−5).','f⁻¹(x)=2+√(x−5), x≥5; range-nya y≥2.'])
add(1,'A4','transform','Combined transformation','Transformasi gabungan',
'P=(1,2), Q=(3,−1), R=(5,4) on y=f(x) become P′=(4,5), Q′=(6,−4), R′=(8,11) under y=af(x−h)+k. Find h,a,k and check all three points.',
'P=(1,2), Q=(3,−1), R=(5,4) pada y=f(x) menjadi P′=(4,5), Q′=(6,−4), R′=(8,11) oleh y=af(x−h)+k. Tentukan h,a,k dan cek ketiga titik.',
['All input coordinates increase by 3, so h=3.','From P,Q: 2a+k=5 and −a+k=−4 → 3a=9 → a=3, k=−1.','y=3f(x−3)−1. Check P: 3(2)−1=5; Q: 3(−1)−1=−4; R: 3(4)−1=11.'],
['Semua koordinat input bertambah 3, sehingga h=3.','Dari P,Q: 2a+k=5 dan −a+k=−4 → 3a=9 → a=3, k=−1.','y=3f(x−3)−1. Cek P: 3(2)−1=5; Q: 3(−1)−1=−4; R: 3(4)−1=11.'])
add(1,'A5','inverse','Open-boundary quadratic inverse','Invers kuadrat dengan batas terbuka',
'Let h(x)=(2x−5)²+3 with x<5/2. Find its range and inverse, state the inverse domain/range, and explain the required square-root branch.',
'Diberikan h(x)=(2x−5)²+3 dengan x<5/2. Tentukan range dan invers, domain/range invers, serta jelaskan pilihan cabang akar.',
['Since 2x−5<0 and the vertex is excluded, R_h=(3,∞).','From y−3=(2x−5)², take 2x−5=−√(y−3).','h⁻¹(x)=(5−√(x−3))/2; D_(h⁻¹)=(3,∞), R_(h⁻¹)=(−∞,5/2).','The negative branch is forced by the original restriction 2x−5<0.'],
['Karena 2x−5<0 dan puncak dikeluarkan, R_h=(3,∞).','Dari y−3=(2x−5)², pilih 2x−5=−√(y−3).','h⁻¹(x)=(5−√(x−3))/2; D_(h⁻¹)=(3,∞), R_(h⁻¹)=(−∞,5/2).','Cabang negatif diwajibkan oleh pembatasan asal 2x−5<0.'])
add(1,'A6','composition','Compatibility for every input','Kompatibilitas untuk semua input',
'Let f(x)=x²+a for 0≤x≤3 and g(x)=√(13−x). Find all a for which gf(x) is defined for every input of f. At the largest possible a, find the range of gf.',
'Diberikan f(x)=x²+a untuk 0≤x≤3 dan g(x)=√(13−x). Tentukan semua a agar gf(x) terdefinisi untuk setiap input f. Pada a terbesar, tentukan range gf.',
['Require 13−(x²+a)≥0 for every x∈[0,3].','The largest x² is 9, so 9+a≤13 → a≤4.','At a=4, gf(x)=√(9−x²) on [0,3], with range [0,3].'],
['Syarat 13−(x²+a)≥0 untuk setiap x∈[0,3].','Nilai x² terbesar 9, sehingga 9+a≤13 → a≤4.','Pada a=4, gf(x)=√(9−x²) di [0,3], dengan range [0,3].'])
add(1,'A7','inverse','Graph, inverse and translation','Grafik, invers, dan translasi',
'A strictly increasing f has domain [1,5] and contains (1,−2), (3,4), (5,7); endpoint values are min/max. State its range, the inverse domain/range and three inverse points, then their images on y=f⁻¹(x)+2.',
'Fungsi naik tegas f berdomain [1,5] dan melalui (1,−2), (3,4), (5,7); nilai ujung adalah min/maks. Tentukan range, domain/range invers, tiga titik invers, lalu bayangannya pada y=f⁻¹(x)+2.',
['With the stated endpoint min/max, R_f=[−2,7]. Therefore D_(f⁻¹)=[−2,7], R_(f⁻¹)=[1,5].','Swap coordinates: (−2,1), (4,3), (7,5).','Add 2 to each output: (−2,3), (4,5), (7,7).'],
['Dengan min/maks ujung yang diberikan, R_f=[−2,7]. Jadi D_(f⁻¹)=[−2,7], R_(f⁻¹)=[1,5].','Tukar koordinat: (−2,1), (4,3), (7,5).','Tambah 2 pada tiap output: (−2,3), (4,5), (7,7).'])
add(1,'A8','transform','Vertical versus horizontal','Vertikal versus horizontal',
'A point (a,b) lies on y=f(x). (a) Find its image under y=2f(x), y=f(2x), and y=f(−2x). (b) Use (4,3). (c) Explain the difference. (d) Describe y=f(−2x) geometrically.',
'Titik (a,b) terletak pada y=f(x). (a) Tentukan bayangannya oleh y=2f(x), y=f(2x), dan y=f(−2x). (b) Gunakan (4,3). (c) Jelaskan perbedaannya. (d) Deskripsikan y=f(−2x) secara geometri.',
['2f(x) maps (a,b) to (a,2b). f(2x) requires 2x=a, so gives (a/2,b).','f(−2x) requires −2x=a, giving (−a/2,b).','For (4,3), the points are (4,6), (2,3), (−2,3).','Outside multiplication changes outputs; inside multiplication changes input coordinates inversely. f(−2x) reflects in the y-axis and compresses horizontally by factor 1/2.'],
['2f(x) memetakan (a,b) ke (a,2b). f(2x) mensyaratkan 2x=a, sehingga menjadi (a/2,b).','f(−2x) mensyaratkan −2x=a, menghasilkan (−a/2,b).','Untuk (4,3), titik-titiknya (4,6), (2,3), (−2,3).','Perkalian di luar mengubah output; di dalam mengubah koordinat input secara terbalik. f(−2x) merefleksikan terhadap sumbu-y dan memampatkan horizontal dengan faktor 1/2.'])
add(1,'A9','composition','Two composition restrictions','Dua pembatasan komposisi',
'Let f(x)=1/(x−2) and g(x)=√(x+1). Find fg(x) and its domain; then gf(x) and its domain as intervals or inequalities.',
'Diberikan f(x)=1/(x−2) dan g(x)=√(x+1). Tentukan fg(x) dan domainnya, lalu gf(x) dan domainnya dalam interval atau pertidaksamaan.',
['fg(x)=1/(√(x+1)−2). Require x≥−1 and √(x+1)≠2 → x≠3.','D_fg=[−1,3)∪(3,∞).','gf(x)=√(1/(x−2)+1)=√((x−1)/(x−2)). Require x≠2 and (x−1)/(x−2)≥0.','Sign analysis at 1 and 2 gives D_gf=(−∞,1]∪(2,∞).'],
['fg(x)=1/(√(x+1)−2). Syarat x≥−1 dan √(x+1)≠2 → x≠3.','D_fg=[−1,3)∪(3,∞).','gf(x)=√(1/(x−2)+1)=√((x−1)/(x−2)). Syarat x≠2 dan (x−1)/(x−2)≥0.','Analisis tanda di 1 dan 2 memberi D_gf=(−∞,1]∪(2,∞).'])
add(1,'A10','composition','Reconstruction and inverse chain','Rekonstruksi dan rantai invers',
'Let f(x)=ax+b, a≠0, and g(x)=x−2. Given f⁻¹(7)=3 and fg(6)=10, find f, f⁻¹, h(x)=f⁻¹(g(x)), and the x for which h(x)=5.',
'Diberikan f(x)=ax+b, a≠0, dan g(x)=x−2. Jika f⁻¹(7)=3 dan fg(6)=10, tentukan f, f⁻¹, h(x)=f⁻¹(g(x)), dan x saat h(x)=5.',
['f⁻¹(7)=3 means f(3)=7. Also g(6)=4, so f(4)=10.','3a+b=7 and 4a+b=10 → a=3, b=−2; f(x)=3x−2.','f⁻¹(x)=(x+2)/3; h(x)=((x−2)+2)/3=x/3.','h(x)=5 → x=15.'],
['f⁻¹(7)=3 berarti f(3)=7. Juga g(6)=4, sehingga f(4)=10.','3a+b=7 dan 4a+b=10 → a=3, b=−2; f(x)=3x−2.','f⁻¹(x)=(x+2)/3; h(x)=((x−2)+2)/3=x/3.','h(x)=5 → x=15.'])
add(2,'C1','polynomial','Read a cubic from factors','Baca kubik dari faktor',
'Let f(x)=(x+4)(x−1)(x−3). Without a value table, state (a) all x-intercepts, (b) the y-intercept, (c) crossing/touching at each root, (d) end behaviour.',
'Diberikan f(x)=(x+4)(x−1)(x−3). Tanpa tabel nilai, tentukan (a) semua intersep-x, (b) intersep-y, (c) melintas/menyentuh pada tiap akar, (d) perilaku ujung.',
['Roots −4,1,3 give intercepts (−4,0),(1,0),(3,0).','f(0)=4(−1)(−3)=12, so the y-intercept is (0,12).','All roots are simple crossings. The leading term is x³: left down, right up.'],
['Akar −4,1,3 memberi intersep (−4,0),(1,0),(3,0).','f(0)=4(−1)(−3)=12, sehingga intersep-y adalah (0,12).','Semua akar sederhana melintas. Suku utama x³: kiri turun, kanan naik.'],'cubic')
add(2,'C2','polynomial','Repeated root','Akar berulang',
'Let g(x)=−(x+2)²(x−5). Find the roots, identify touching/crossing, find the y-intercept, and describe end behaviour.',
'Diberikan g(x)=−(x+2)²(x−5). Tentukan akar, perilaku menyentuh/melintas, intersep-y, dan perilaku ujung.',
['The roots are −2 (multiplicity 2) and 5 (multiplicity 1).','The graph touches at −2 and crosses at 5; g(0)=−4(−5)=20.','The leading term is −x³: left up, right down.'],
['Akarnya −2 (multiplicity 2) dan 5 (multiplicity 1).','Grafik menyentuh pada −2 dan melintas pada 5; g(0)=−4(−5)=20.','Suku utama −x³: kiri naik, kanan turun.'])
add(2,'C3','polynomial','Quartic structure','Struktur kuartik',
'Let h(x)=−2(x−1)(x+3)(x−4)(x+1). State all roots, crossing/touching behaviour, the y-intercept, and end behaviour.',
'Diberikan h(x)=−2(x−1)(x+3)(x−4)(x+1). Tentukan semua akar, perilaku melintas/menyentuh, intersep-y, dan perilaku ujung.',
['The roots are −3,−1,1,4. All are simple crossings.','h(0)=−2(−1)(3)(−4)(1)=−24, so the y-intercept is (0,−24).','The leading term is −2x⁴: both ends down.'],
['Akarnya −3,−1,1,4. Semuanya sederhana dan melintas.','h(0)=−2(−1)(3)(−4)(1)=−24, sehingga intersep-y (0,−24).','Suku utama −2x⁴: kedua ujung turun.'])
add(2,'C4','polynomial','Sign from a cubic','Tanda dari fungsi kubik',
'Let f(x)=x(x−2)(x+3). Without expanding, determine where f(x)>0 and where f(x)<0.',
'Diberikan f(x)=x(x−2)(x+3). Tanpa mengembangkan, tentukan daerah f(x)>0 dan f(x)<0.',
['Order the simple roots: −3,0,2. The rightmost interval has positive sign.','Crossing each simple root changes sign: −,+,−,+ from left to right.','f>0 on (−3,0)∪(2,∞); f<0 on (−∞,−3)∪(0,2).'],
['Urutkan akar sederhana: −3,0,2. Interval paling kanan bertanda positif.','Setiap akar sederhana mengubah tanda: −,+,−,+ dari kiri ke kanan.','f>0 pada (−3,0)∪(2,∞); f<0 pada (−∞,−3)∪(0,2).'])
add(2,'C5','rational','Reciprocal structure','Struktur reciprocal',
'For f(x)=−3/x, find the domain, both asymptotes, the sign for x<0 and x>0, and the quadrants containing the graph.',
'Untuk f(x)=−3/x, tentukan domain, kedua asimtot, tanda saat x<0 dan x>0, serta kuadran grafik.',
['The denominator excludes 0: D=ℝ∖{0}.','The asymptotes are x=0 and y=0.','For x<0 the output is positive; for x>0 it is negative. The graph lies in quadrants II and IV.'],
['Penyebut mengeluarkan 0: D=ℝ∖{0}.','Asimtotnya x=0 dan y=0.','Untuk x<0 output positif; untuk x>0 output negatif. Grafik berada di kuadran II dan IV.'])
add(2,'C6','rational','Translated reciprocal','Reciprocal yang ditranslasi',
'For f(x)=4/(x+2)+1, find the domain, vertical/horizontal asymptotes, x-intercept and y-intercept.',
'Untuk f(x)=4/(x+2)+1, tentukan domain, asimtot vertikal/horizontal, intersep-x, dan intersep-y.',
['D=ℝ∖{−2}; the asymptotes are x=−2 and y=1.','Set f(x)=0: 4/(x+2)=−1 → x=−6, giving (−6,0).','f(0)=4/2+1=3, giving (0,3).'],
['D=ℝ∖{−2}; asimtotnya x=−2 dan y=1.','Ambil f(x)=0: 4/(x+2)=−1 → x=−6, sehingga (−6,0).','f(0)=4/2+1=3, sehingga (0,3).'],'reciprocal')
add(2,'C7','rational','Simple rational graph','Grafik rasional sederhana',
'Let f(x)=(x−4)/(x+1). State its domain; rewrite as A+B/(x+1); find both asymptotes, both axis intercepts, and its positive/negative intervals.',
'Diberikan f(x)=(x−4)/(x+1). Nyatakan domain; tulis sebagai A+B/(x+1); tentukan kedua asimtot, intersep sumbu, dan interval positif/negatif.',
['D=ℝ∖{−1}. Since x−4=(x+1)−5, f(x)=1−5/(x+1).','Asymptotes: x=−1,y=1; intercepts: (4,0),(0,−4).','The sign is positive for x<−1 or x>4, and negative for −1<x<4.'],
['D=ℝ∖{−1}. Karena x−4=(x+1)−5, f(x)=1−5/(x+1).','Asimtot: x=−1,y=1; intersep: (4,0),(0,−4).','Tanda positif untuk x<−1 atau x>4, negatif untuk −1<x<4.'])
add(2,'C8','intersections','Intersections as solutions','Perpotongan sebagai solusi',
'Find the intersection points of y=x(x−2)(x+2) and y=5x. Hence state the number of real solutions of x(x−2)(x+2)=5x.',
'Tentukan titik potong y=x(x−2)(x+2) dan y=5x, lalu jumlah solusi real x(x−2)(x+2)=5x.',
['Set outputs equal: x(x²−4)=5x → x(x²−9)=0.','x=−3,0,3. Substitute into y=5x.','Intersections: (−3,−15),(0,0),(3,15); three real solutions.'],
['Samakan output: x(x²−4)=5x → x(x²−9)=0.','x=−3,0,3. Substitusi ke y=5x.','Titik potong: (−3,−15),(0,0),(3,15); tiga solusi real.'])
add(2,'C9','polynomial','Polynomial inequality','Pertidaksamaan polinom',
'Solve (x+2)(x−1)(x−4)>0.','Selesaikan (x+2)(x−1)(x−4)>0.',
['The simple roots are −2,1,4.','The positive-leading cubic has signs −,+,−,+ on the four intervals.','Strict positivity gives (−2,1)∪(4,∞); exclude the roots.'],
['Akar sederhananya −2,1,4.','Kubik dengan koefisien utama positif bertanda −,+,−,+ pada empat interval.','Positif tegas memberi (−2,1)∪(4,∞); akar dikeluarkan.'])
add(2,'C10','transform','Transform reciprocal features','Transformasi ciri reciprocal',
'Let g(x)=2/(x−1)−3 and h(x)=g(x+4)+5. Find the vertical/horizontal asymptotes and x-intercept of h.',
'Diberikan g(x)=2/(x−1)−3 dan h(x)=g(x+4)+5. Tentukan asimtot vertikal/horizontal dan intersep-x h.',
['h(x)=2/((x+4)−1)−3+5=2/(x+3)+2.','The asymptotes are x=−3 and y=2.','Set 2/(x+3)+2=0 → x=−4; the x-intercept is (−4,0).'],
['h(x)=2/((x+4)−1)−3+5=2/(x+3)+2.','Asimtotnya x=−3 dan y=2.','Ambil 2/(x+3)+2=0 → x=−4; intersep-x adalah (−4,0).'])
add(2,'H1','polynomial','Reconstruct a cubic','Rekonstruksi kubik',
'A cubic crosses at x=−3, touches at x=2, and contains (3,−24). Find a cubic satisfying these conditions and describe its end behaviour.',
'Sebuah kubik melintas pada x=−3, menyentuh pada x=2, dan melalui (3,−24). Tentukan kubiknya dan perilaku ujung.',
['The degree-3 structure is f(x)=k(x+3)(x−2)².','At (3,−24): −24=k(6)(1), so k=−4.','f(x)=−4(x+3)(x−2)². The negative-leading cubic has left end up and right end down.'],
['Struktur derajat 3 adalah f(x)=k(x+3)(x−2)².','Pada (3,−24): −24=k(6)(1), sehingga k=−4.','f(x)=−4(x+3)(x−2)². Kubik negatif berujung kiri naik dan kanan turun.'])
add(2,'H2','polynomial','Reconstruct a quartic','Rekonstruksi kuartik',
'A quartic touches at x=−2, crosses at x=1 and x=4, and contains (0,−32). Find a least-degree polynomial with these features and its end behaviour.',
'Sebuah kuartik menyentuh pada x=−2, melintas pada x=1 dan x=4, serta melalui (0,−32). Tentukan polinom berderajat minimum dengan ciri tersebut dan perilaku ujungnya.',
['The least-degree form is f(x)=k(x+2)²(x−1)(x−4).','f(0)=16k=−32 → k=−2.','f(x)=−2(x+2)²(x−1)(x−4); its negative quartic leading term sends both ends down.'],
['Bentuk derajat minimum f(x)=k(x+2)²(x−1)(x−4).','f(0)=16k=−32 → k=−2.','f(x)=−2(x+2)²(x−1)(x−4); suku utama kuartik negatif membuat kedua ujung turun.'])
add(2,'H3','rational','Reconstruct a reciprocal','Rekonstruksi reciprocal',
'A reciprocal-type function has asymptotes x=3 and y=2 and an x-intercept at x=1. Find f(x)=a/(x−3)+2 and its y-intercept.',
'Fungsi bertipe reciprocal berasimtot x=3 dan y=2, serta berintersep-x pada x=1. Tentukan f(x)=a/(x−3)+2 dan intersep-y-nya.',
['Use the root: 0=a/(1−3)+2=−a/2+2.','a=4, so f(x)=4/(x−3)+2.','f(0)=−4/3+2=2/3; the y-intercept is (0,2/3).'],
['Gunakan akar: 0=a/(1−3)+2=−a/2+2.','a=4, sehingga f(x)=4/(x−3)+2.','f(0)=−4/3+2=2/3; intersep-y adalah (0,2/3).'])
add(2,'H4','rational','Rational comparison','Perbandingan rasional',
'Solve (2x+1)/(x−3)>1. Explain why x=3 is excluded.',
'Selesaikan (2x+1)/(x−3)>1. Jelaskan mengapa x=3 dikeluarkan.',
['The original denominator requires x≠3. Move 1 to the left: (x+4)/(x−3)>0.','The critical values are −4 and 3; numerator and denominator have the same sign outside them.','The solution is (−∞,−4)∪(3,∞). x=3 is undefined, not a possible endpoint.'],
['Penyebut awal mensyaratkan x≠3. Pindahkan 1 ke kiri: (x+4)/(x−3)>0.','Nilai kritis −4 dan 3; pembilang dan penyebut bertanda sama di luar keduanya.','Solusinya (−∞,−4)∪(3,∞). x=3 tidak terdefinisi, sehingga tidak dapat disertakan.'])
add(2,'H5','intersections','Line–cubic intersections','Perpotongan garis–kubik',
'Find all intersections of y=(x−1)(x+1)(x−3) and y=x−3. Interpret graphically.',
'Tentukan semua titik potong y=(x−1)(x+1)(x−3) dan y=x−3. Tafsirkan secara grafik.',
['Set equal and factor without dividing by x−3: (x−3)[(x−1)(x+1)−1]=0.','(x−3)(x²−2)=0 → x=3,√2,−√2.','Substitute y=x−3: (3,0),(√2,√2−3),(−√2,−√2−3). Three distinct intersections.'],
['Samakan dan faktorkan tanpa membagi dengan x−3: (x−3)[(x−1)(x+1)−1]=0.','(x−3)(x²−2)=0 → x=3,√2,−√2.','Substitusi y=x−3: (3,0),(√2,√2−3),(−√2,−√2−3). Tiga titik potong berbeda.'])
add(2,'H6','intersections','Number of solutions from turning levels','Jumlah solusi dari level titik balik',
'A positive-leading cubic has local maximum value 4 and local minimum value −3. Count distinct real solutions of f(x)=k for (a) k>4, (b) k=4, (c) −3<k<4, (d) k=−3, (e) k<−3.',
'Kubik berkoefisien utama positif mempunyai maksimum lokal 4 dan minimum lokal −3. Hitung solusi real berbeda f(x)=k untuk (a) k>4, (b) k=4, (c) −3<k<4, (d) k=−3, (e) k<−3.',
['A horizontal line above the maximum or below the minimum meets only one branch.','At either turning level it is tangent at one point and crosses at one other point.','Between the turning levels it crosses three times. Counts (a)–(e): 1,2,3,2,1.'],
['Garis horizontal di atas maksimum atau di bawah minimum hanya memotong satu cabang.','Pada salah satu level titik balik, garis menyinggung satu titik dan melintas di satu titik lain.','Di antara kedua level, ada tiga perpotongan. Jumlah (a)–(e): 1,2,3,2,1.'])
add(2,'H7','rational','Find the reciprocal parameter','Mencari parameter reciprocal',
'Let f(x)=a/(x+1)−2 and f(1)=1. Find a, both asymptotes and both axis intercepts.',
'Diberikan f(x)=a/(x+1)−2 dan f(1)=1. Tentukan a, kedua asimtot, dan kedua intersep sumbu.',
['1=a/2−2 → a=6. Thus f(x)=6/(x+1)−2.','The asymptotes are x=−1 and y=−2.','Set f=0 → x=2. Also f(0)=4. Intercepts: (2,0),(0,4).'],
['1=a/2−2 → a=6. Jadi f(x)=6/(x+1)−2.','Asimtotnya x=−1 dan y=−2.','Ambil f=0 → x=2. Juga f(0)=4. Intersep: (2,0),(0,4).'])
add(2,'H8','intersections','Can the graphs intersect?','Dapatkah grafik berpotongan?',
'Determine whether y=6/(x+2) and y=2−x intersect. Justify algebraically and interpret graphically.',
'Tentukan apakah y=6/(x+2) dan y=2−x berpotongan. Jelaskan secara aljabar dan grafik.',
['Require x≠−2. Equating outputs gives 6=(2−x)(x+2)=4−x².','Thus x²=−2, which has no real solution.','There is no real intersection point between the two graphs.'],
['Syarat x≠−2. Menyamakan output memberi 6=(2−x)(x+2)=4−x².','Jadi x²=−2, tanpa solusi real.','Kedua grafik tidak mempunyai titik potong real.'])
add(2,'H9','rational','Reconstruct from mixed features','Rekonstruksi dari ciri campuran',
'Let f(x)=a/(x−1)+k have x-intercept x=4 and y-intercept (0,4). Find a,k, its horizontal asymptote and where f(x)>0.',
'Fungsi f(x)=a/(x−1)+k berintersep-x pada x=4 dan berintersep-y (0,4). Tentukan a,k, asimtot horizontal, dan daerah f(x)>0.',
['From f(4)=0: a/3+k=0 → k=−a/3. From f(0)=4: −a+k=4.','Solve to obtain a=−3,k=1. Thus f(x)=1−3/(x−1)=(x−4)/(x−1).','The horizontal asymptote is y=1; f>0 for x<1 or x>4.'],
['Dari f(4)=0: a/3+k=0 → k=−a/3. Dari f(0)=4: −a+k=4.','Diperoleh a=−3,k=1. Jadi f(x)=1−3/(x−1)=(x−4)/(x−1).','Asimtot horizontal y=1; f>0 untuk x<1 atau x>4.'])
add(2,'H10','transform','Transformed cubic roots','Akar kubik yang ditransformasi',
'A cubic f has positive leading coefficient and simple roots −2,1,5. Define g(x)=−f(2x+4). Find its roots, crossing/touching behaviour and end behaviour.',
'Kubik f berkoefisien utama positif dengan akar sederhana −2,1,5. Didefinisikan g(x)=−f(2x+4). Tentukan akar, perilaku melintas/menyentuh, dan perilaku ujung.',
['Set 2x+4=r for each original root r. The new roots are −3,−3/2,1/2.','An invertible linear input transformation preserves multiplicities, so all remain crossings.','The input factor 2 keeps the leading sign, but the outside minus makes it negative: left up, right down.'],
['Ambil 2x+4=r untuk setiap akar asal r. Akar baru −3,−3/2,1/2.','Transformasi input linear yang invertibel mempertahankan multiplicity, jadi semuanya tetap melintas.','Faktor input 2 menjaga tanda utama, tetapi minus di luar membuatnya negatif: kiri naik, kanan turun.'])
add(2,'A1','polynomial','Quartic reconstruction and inequality','Rekonstruksi kuartik dan pertidaksamaan',
'A quartic touches at x=−3, crosses at x=1 and x=4, and passes through (0,72). Construct the least-degree polynomial, state end behaviour, and solve f(x)<0.',
'Kuartik menyentuh pada x=−3, melintas pada x=1 dan x=4, serta melalui (0,72). Bentuk polinom berderajat minimum, nyatakan perilaku ujung, dan selesaikan f(x)<0.',
['f(x)=k(x+3)²(x−1)(x−4). From f(0)=72: 36k=72 → k=2.','f(x)=2(x+3)²(x−1)(x−4), with both ends up.','The squared factor is positive away from −3 and does not change sign. The product is negative exactly for 1<x<4.'],
['f(x)=k(x+3)²(x−1)(x−4). Dari f(0)=72: 36k=72 → k=2.','f(x)=2(x+3)²(x−1)(x−4), dengan kedua ujung naik.','Faktor kuadrat positif di luar −3 dan tidak mengubah tanda. Hasil kali negatif tepat untuk 1<x<4.'])
add(2,'A2','intersections','Parameterised line–parabola intersections','Parameter perpotongan garis–parabola',
'Consider y=x²−2x+5 and y=mx+3. Find m giving (a) two distinct real intersections, (b) exactly one, (c) none. Interpret the boundary cases.',
'Tinjau y=x²−2x+5 dan y=mx+3. Tentukan m yang memberi (a) dua titik potong real berbeda, (b) tepat satu, (c) tidak ada. Tafsirkan kasus batas.',
['Equating gives x²−(m+2)x+2=0; Δ=(m+2)²−8.','Two intersections: m<−2−2√2 or m>−2+2√2.','One: m=−2±2√2; each boundary line is tangent.','None: −2−2√2<m<−2+2√2.'],
['Menyamakan memberi x²−(m+2)x+2=0; Δ=(m+2)²−8.','Dua perpotongan: m<−2−2√2 atau m>−2+2√2.','Satu: m=−2±2√2; tiap garis batas menyinggung parabola.','Tidak ada: −2−2√2<m<−2+2√2.'])
add(2,'A3','rational','Reconstruct a rational function','Rekonstruksi fungsi rasional',
'A reciprocal-type function has asymptotes x=2 and y=−1 and contains (0,3). Find the function, its x-intercept, and solve f(x)>0.',
'Fungsi bertipe reciprocal berasimtot x=2 dan y=−1, melalui (0,3). Tentukan fungsi, intersep-x, dan solusi f(x)>0.',
['f(x)=a/(x−2)−1. From (0,3): 3=−a/2−1 → a=−8.','f(x)=−8/(x−2)−1=−(x+6)/(x−2). The root is x=−6.','Sign analysis at −6 and 2 gives f>0 on (−6,2).'],
['f(x)=a/(x−2)−1. Dari (0,3): 3=−a/2−1 → a=−8.','f(x)=−8/(x−2)−1=−(x+6)/(x−2). Akarnya x=−6.','Analisis tanda di −6 dan 2 memberi f>0 pada (−6,2).'])
add(2,'A4','transform','Transform a rational graph','Transformasi grafik rasional',
'Let f(x)=3/(x−2)−1 and g(x)=−2f(3x+6). Without a value table find the domain, both asymptotes and both axis intercepts of g.',
'Diberikan f(x)=3/(x−2)−1 dan g(x)=−2f(3x+6). Tanpa tabel nilai, tentukan domain, kedua asimtot, dan intersep sumbu g.',
['g(x)=−6/(3x+4)+2. The denominator excludes x=−4/3.','Asymptotes: x=−4/3 and y=2; D_g=ℝ∖{−4/3}.','For the root, 3x+6=5, so x=−1/3. Also g(0)=−6/4+2=1/2.','Intercepts: (−1/3,0) and (0,1/2).'],
['g(x)=−6/(3x+4)+2. Penyebut mengeluarkan x=−4/3.','Asimtot: x=−4/3 dan y=2; D_g=ℝ∖{−4/3}.','Untuk akar, 3x+6=5, sehingga x=−1/3. Juga g(0)=−6/4+2=1/2.','Intersep: (−1/3,0) dan (0,1/2).'])
add(2,'A5','rational','Compare two rational functions','Bandingkan dua fungsi rasional',
'Solve 2/(x−1)>1/(x+2). Show every critical value and exclude undefined inputs.',
'Selesaikan 2/(x−1)>1/(x+2). Tunjukkan semua nilai kritis dan keluarkan input tak terdefinisi.',
['Domain: x≠1,−2. Combine the difference: (x+5)/((x−1)(x+2))>0.','Order critical values −5,−2,1; signs from left to right are −,+,−,+.','Strict positivity gives (−5,−2)∪(1,∞).'],
['Domain: x≠1,−2. Gabungkan selisih: (x+5)/((x−1)(x+2))>0.','Urutkan nilai kritis −5,−2,1; tanda dari kiri ke kanan −,+,−,+.','Positif tegas memberi (−5,−2)∪(1,∞).'])
add(2,'A6','intersections','Parameterised cubic–line intersections','Parameter perpotongan kubik–garis',
'For f(x)=x³−3x and y=kx, find k giving (a) three distinct real intersection points, (b) exactly one. Explain the boundary.',
'Untuk f(x)=x³−3x dan y=kx, tentukan k yang memberi (a) tiga titik potong real berbeda, (b) tepat satu. Jelaskan batasnya.',
['Equate: x³−3x=kx → x[x²−(k+3)]=0. Input 0 is always a solution.','If k>−3, x=±√(k+3) are distinct and nonzero: three intersections.','If k≤−3, only x=0 is real and distinct. At k=−3 it is a triple root, still one distinct point.'],
['Samakan: x³−3x=kx → x[x²−(k+3)]=0. Input 0 selalu solusi.','Jika k>−3, x=±√(k+3) berbeda dan bukan nol: tiga perpotongan.','Jika k≤−3, hanya x=0 yang real dan berbeda. Pada k=−3 akarnya rangkap tiga, tetap satu titik berbeda.'])
add(2,'A7','polynomial','Repeated-root reconstruction','Rekonstruksi akar berulang',
'A monic cubic has repeated root x=2 and constant term −6. Its third root is real. Find that root, expand as x³+ax²+bx−6, and describe behaviour at every root.',
'Kubik monik mempunyai akar berulang x=2 dan konstanta −6. Akar ketiganya real. Tentukan akar itu, kembangkan menjadi x³+ax²+bx−6, dan jelaskan perilaku pada tiap akar.',
['Write f(x)=(x−2)²(x−r). The constant term is −4r=−6, so r=3/2.','Expansion gives f(x)=x³−(11/2)x²+10x−6; a=−11/2,b=10.','It crosses at x=3/2 and touches at x=2.'],
['Tulis f(x)=(x−2)²(x−r). Konstanta −4r=−6, sehingga r=3/2.','Ekspansi memberi f(x)=x³−(11/2)x²+10x−6; a=−11/2,b=10.','Grafik melintas pada x=3/2 dan menyentuh pada x=2.'])
add(2,'A8','transform','Transformed quartic structure','Struktur kuartik setelah transformasi',
'Let f(x)=(x+2)²(x−1)(x−4) and g(x)=−f(2x−2). Without expanding, find the roots, touching root, end behaviour, and solve g(x)>0.',
'Diberikan f(x)=(x+2)²(x−1)(x−4) dan g(x)=−f(2x−2). Tanpa ekspansi, tentukan akar, akar sentuh, perilaku ujung, dan solusi g(x)>0.',
['Solve 2x−2=r for r=−2,1,4: roots 0 (double), 3/2,3.','The root 0 touches; 3/2 and 3 cross. The outside minus makes both ends down.','The double factor does not change sign. g(x)>0 exactly for 3/2<x<3.'],
['Selesaikan 2x−2=r untuk r=−2,1,4: akar 0 (ganda), 3/2,3.','Akar 0 menyentuh; 3/2 dan 3 melintas. Minus di luar membuat kedua ujung turun.','Faktor ganda tidak mengubah tanda. g(x)>0 tepat untuk 3/2<x<3.'])
add(2,'A9','rational','Hole, asymptote and inequality','Lubang, asimtot, dan pertidaksamaan',
'Let r(x)=((x−3)(x+1))/((x−3)(x−2)). State the full domain, simplify on permitted inputs, identify both asymptotes and the hole, find the x-intercept, and solve r(x)>0.',
'Diberikan r(x)=((x−3)(x+1))/((x−3)(x−2)). Nyatakan domain lengkap, sederhanakan pada input sah, tentukan kedua asimtot dan lubang, intersep-x, dan solusi r(x)>0.',
['The original domain excludes 2 and 3. For permitted x, r(x)=(x+1)/(x−2)=1+3/(x−2).','Asymptotes: x=2 and y=1. At the cancelled input x=3, the limiting height is 4: hole (3,4).','The x-intercept is (−1,0). The simplified sign is positive for x<−1 or x>2.','Keep the original exclusion x=3: (−∞,−1)∪(2,3)∪(3,∞).'],
['Domain awal mengeluarkan 2 dan 3. Untuk x sah, r(x)=(x+1)/(x−2)=1+3/(x−2).','Asimtot: x=2 dan y=1. Pada input tercoret x=3, tinggi limitnya 4: lubang (3,4).','Intersep-x adalah (−1,0). Tanda bentuk sederhana positif untuk x<−1 atau x>2.','Pertahankan larangan awal x=3: (−∞,−1)∪(2,3)∪(3,∞).'],'hole')
add(2,'A10','rational','Reconstruct then solve','Rekonstruksi lalu selesaikan',
'Let f(x)=(ax+b)/(x−2), with horizontal asymptote y=3 and x-intercept x=−1. Find a,b, rewrite in reciprocal form, state both asymptotes, and solve f(x)>6.',
'Diberikan f(x)=(ax+b)/(x−2), berasimtot horizontal y=3 dan berintersep-x pada x=−1. Tentukan a,b, bentuk reciprocal, kedua asimtot, dan solusi f(x)>6.',
['The leading-coefficient ratio gives a=3. The numerator vanishes at −1: −3+b=0 → b=3.','f(x)=(3x+3)/(x−2)=3+9/(x−2), x≠2. Asymptotes x=2,y=3.','f(x)>6 → −3(x−5)/(x−2)>0 → (x−5)/(x−2)<0.','The solution is 2<x<5.'],
['Rasio koefisien utama memberi a=3. Pembilang nol di −1: −3+b=0 → b=3.','f(x)=(3x+3)/(x−2)=3+9/(x−2), x≠2. Asimtot x=2,y=3.','f(x)>6 → −3(x−5)/(x−2)>0 → (x−5)/(x−2)<0.','Solusinya 2<x<5.'])
add(3,'C1','exponential','Linear or exponential?','Linear atau eksponen?',
'A: 12,17,22,27,… B: 12,18,27,40.5,…\n(a) Which is linear? (b) Which is exponential? (c) State the constant difference/ratio.',
'A: 12,17,22,27,… B: 12,18,27,40.5,…\n(a) Mana yang linear? (b) Mana yang eksponen? (c) Nyatakan selisih/rasio tetapnya.',
['A has constant difference 17−12=22−17=5, so it is linear.','B has constant ratio 18/12=27/18=3/2, so it is exponential.','Equal input steps add 5 in A but multiply by 1.5 in B.'],
['A mempunyai selisih tetap 17−12=22−17=5, sehingga linear.','B mempunyai rasio tetap 18/12=27/18=3/2, sehingga eksponen.','Langkah input yang sama menambah 5 pada A tetapi mengalikan 1.5 pada B.'])
add(3,'C2','exponential','Build an exponential function','Membangun fungsi eksponen',
'An exponential has initial value 7. Each unit increase in x multiplies its output by 3. Write f(x)=Abˣ, find f(2), and classify growth/decay.',
'Fungsi eksponen bernilai awal 7. Setiap kenaikan x satu satuan mengalikan output dengan 3. Tulis f(x)=Abˣ, hitung f(2), dan tentukan pertumbuhan/peluruhan.',
['The initial value gives A=7; the multiplier gives b=3.','f(x)=7·3ˣ and f(2)=7·9=63.','Since b=3>1 and A>0, it models growth.'],
['Nilai awal memberi A=7; pengali memberi b=3.','f(x)=7·3ˣ dan f(2)=7·9=63.','Karena b=3>1 dan A>0, model ini bertumbuh.'])
add(3,'C3','exponential','Read the equation','Baca persamaannya',
'For f(x)=5(3/2)ˣ, determine the y-intercept, domain, range, horizontal asymptote and whether it increases or decreases.',
'Untuk f(x)=5(3/2)ˣ, tentukan intersep-y, domain, range, asimtot horizontal, dan apakah naik atau turun.',
['f(0)=5, so the y-intercept is (0,5).','D=ℝ; R=(0,∞); horizontal asymptote y=0.','The positive coefficient and base 3/2>1 make it increasing.'],
['f(0)=5, sehingga intersep-y (0,5).','D=ℝ; R=(0,∞); asimtot horizontal y=0.','Koefisien positif dan basis 3/2>1 membuat fungsi naik.'])
add(3,'C4','exponential','Transformed exponential','Eksponen yang ditransformasi',
'For f(x)=2·3^(x−1)−6, find the horizontal asymptote, range, f(1) and x-intercept.',
'Untuk f(x)=2·3^(x−1)−6, tentukan asimtot horizontal, range, f(1), dan intersep-x.',
['The vertical shift gives asymptote y=−6; the positive exponential term gives R=(−6,∞).','f(1)=2·3⁰−6=−4.','For the root: 2·3^(x−1)=6 → 3^(x−1)=3 → x=2, giving (2,0).'],
['Geser vertikal memberi asimtot y=−6; suku eksponen positif memberi R=(−6,∞).','f(1)=2·3⁰−6=−4.','Untuk akar: 2·3^(x−1)=6 → 3^(x−1)=3 → x=2, sehingga (2,0).'],'exponential')
add(3,'C5','equations','Common base','Samakan basis',
'Solve 8^(x−1)=4^(x+1).','Selesaikan 8^(x−1)=4^(x+1).',
['Write 8=2³ and 4=2²: 2^(3x−3)=2^(2x+2).','Equal powers of the same valid base have equal exponents: 3x−3=2x+2.','x=5. Check: 8⁴=4⁶=4096.'],
['Tulis 8=2³ dan 4=2²: 2^(3x−3)=2^(2x+2).','Pangkat dari basis sah yang sama disamakan: 3x−3=2x+2.','x=5. Cek: 8⁴=4⁶=4096.'])
add(3,'C6','logarithm','Exponential and logarithmic forms','Bentuk eksponen dan logaritma',
'Rewrite each in the other form: (a) 5³=125, (b) log₂(1/8)=−3, (c) 7⁰=1.',
'Ubah masing-masing ke bentuk lainnya: (a) 5³=125, (b) log₂(1/8)=−3, (c) 7⁰=1.',
['Use aʸ=x ⇔ logₐx=y.','(a) log₅125=3. (b) 2⁻³=1/8.','(c) log₇1=0. The argument is positive in every case.'],
['Gunakan aʸ=x ⇔ logₐx=y.','(a) log₅125=3. (b) 2⁻³=1/8.','(c) log₇1=0. Semua argumen bernilai positif.'])
add(3,'C7','logarithm','Log laws','Hukum logaritma',
'Evaluate log₂40−log₂5+log₂2 exactly, showing the log-law step.',
'Hitung log₂40−log₂5+log₂2 secara tepat, dengan menunjukkan hukum log.',
['All arguments are positive and the base is the same.','Combine using product and quotient laws: log₂(40·2/5)=log₂16.','Since 2⁴=16, the value is 4.'],
['Semua argumen positif dan basisnya sama.','Gabungkan dengan hukum hasil kali dan hasil bagi: log₂(40·2/5)=log₂16.','Karena 2⁴=16, nilainya 4.'])
add(3,'C8','inverse','Inverse graph','Grafik invers',
'The graph y=4ˣ contains (−1,1/4),(0,1),(1,4). State its inverse, the corresponding three inverse points, its domain/range and vertical asymptote.',
'Grafik y=4ˣ melalui (−1,1/4),(0,1),(1,4). Nyatakan invers, tiga titik invers yang bersesuaian, domain/range, dan asimtot vertikalnya.',
['The inverse is y=log₄x.','Swap coordinates: (1/4,−1),(1,0),(4,1).','Inverse domain (0,∞), range ℝ; vertical asymptote x=0.'],
['Inversnya y=log₄x.','Tukar koordinat: (1/4,−1),(1,0),(4,1).','Domain invers (0,∞), range ℝ; asimtot vertikal x=0.'],'exp-inverse')
add(3,'C9','modelling','Growth model','Model pertumbuhan',
'P(t)=800(1.05)ᵗ. State the initial population and growth rate, find P(3), and interpret 1.05.',
'P(t)=800(1.05)ᵗ. Tentukan populasi awal dan laju pertumbuhan, hitung P(3), dan tafsirkan 1.05.',
['P(0)=800, so the initial population is 800.','1.05=1+0.05, giving 5% growth per time period.','P(3)=800(1.05)³=926.1, approximately 926 individuals. Each period multiplies the previous value by 1.05.'],
['P(0)=800, sehingga populasi awal 800.','1.05=1+0.05, memberi pertumbuhan 5% per periode waktu.','P(3)=800(1.05)³=926.1, sekitar 926 individu. Tiap periode mengalikan nilai sebelumnya dengan 1.05.'])
add(3,'C10','logarithm','Simple log equation','Persamaan log sederhana',
'Solve log₃(x−2)=2. State the domain first.','Selesaikan log₃(x−2)=2. Nyatakan domain terlebih dahulu.',
['The argument must be positive: x−2>0 → x>2.','Rewrite exponentially: x−2=3²=9 → x=11.','11 satisfies the domain and log₃9=2, so it is valid.'],
['Argumen harus positif: x−2>0 → x>2.','Ubah ke eksponen: x−2=3²=9 → x=11.','11 memenuhi domain dan log₃9=2, sehingga sah.'])
add(3,'H1','equations','Choose logarithms','Pilih logaritma',
'Solve 5·2ˣ=17. Give an exact logarithmic answer and a decimal answer to 3 significant figures.',
'Selesaikan 5·2ˣ=17. Berikan jawaban logaritmik tepat dan desimal hingga 3 angka signifikan.',
['Isolate: 2ˣ=17/5.','Take ln: x ln2=ln(17/5), so x=ln(17/5)/ln2.','Numerically x≈1.77 to 3 significant figures.'],
['Isolasi: 2ˣ=17/5.','Ambil ln: x ln2=ln(17/5), sehingga x=ln(17/5)/ln2.','Secara numerik x≈1.77 hingga 3 angka signifikan.'])
add(3,'H2','equations','Quadratic in an exponential','Kuadrat dalam eksponen',
'Solve 9ˣ−10(3ˣ)+9=0. State the substitution explicitly.',
'Selesaikan 9ˣ−10(3ˣ)+9=0. Nyatakan substitusi secara eksplisit.',
['Set u=3ˣ>0; then 9ˣ=u².','u²−10u+9=(u−1)(u−9)=0, so u=1 or 9; both are positive.','Return to x: 3ˣ=1 → x=0; 3ˣ=9 → x=2.'],
['Ambil u=3ˣ>0; maka 9ˣ=u².','u²−10u+9=(u−1)(u−9)=0, sehingga u=1 atau 9; keduanya positif.','Kembali ke x: 3ˣ=1 → x=0; 3ˣ=9 → x=2.'])
add(3,'H3','logarithm','Domain-sensitive log equation','Persamaan log dengan syarat domain',
'Solve log₂(x−1)+log₂(x−3)=3. State the domain first and reject invalid roots.',
'Selesaikan log₂(x−1)+log₂(x−3)=3. Nyatakan domain dahulu dan tolak akar yang tidak sah.',
['Require x−1>0 and x−3>0 simultaneously, so x>3.','Combine: (x−1)(x−3)=2³=8 → x²−4x−5=0.','(x−5)(x+1)=0 gives 5 or −1. Reject −1; the solution is x=5.'],
['Syarat x−1>0 dan x−3>0 secara bersamaan, sehingga x>3.','Gabungkan: (x−1)(x−3)=2³=8 → x²−4x−5=0.','(x−5)(x+1)=0 memberi 5 atau −1. Tolak −1; solusinya x=5.'])
add(3,'H4','logarithm','Transformed logarithm','Logaritma yang ditransformasi',
'For f(x)=3ln(2x−4)−1, find the domain, vertical asymptote, f(5/2) and exact x-intercept.',
'Untuk f(x)=3ln(2x−4)−1, tentukan domain, asimtot vertikal, f(5/2), dan intersep-x tepat.',
['2x−4>0 → x>2; the vertical asymptote is x=2.','At x=5/2, the argument is 1, so f(5/2)=−1.','For f=0: ln(2x−4)=1/3 → x=2+e^(1/3)/2. The intercept is (2+e^(1/3)/2,0).'],
['2x−4>0 → x>2; asimtot vertikal x=2.','Pada x=5/2, argumennya 1, sehingga f(5/2)=−1.','Untuk f=0: ln(2x−4)=1/3 → x=2+e^(1/3)/2. Intersepnya (2+e^(1/3)/2,0).'],'logarithm')
add(3,'H5','inverse','Inverse of a transformed exponential','Invers eksponen yang ditransformasi',
'For f(x)=4e^(x/2)−3, state its domain/range, find f⁻¹(x), then give the inverse domain/range.',
'Untuk f(x)=4e^(x/2)−3, nyatakan domain/range, tentukan f⁻¹(x), lalu domain/range invers.',
['D_f=ℝ; R_f=(−3,∞).','From y+3=4e^(x/2), obtain x=2ln((y+3)/4).','f⁻¹(x)=2ln((x+3)/4); D_(f⁻¹)=(−3,∞), R_(f⁻¹)=ℝ.'],
['D_f=ℝ; R_f=(−3,∞).','Dari y+3=4e^(x/2), diperoleh x=2ln((y+3)/4).','f⁻¹(x)=2ln((x+3)/4); D_(f⁻¹)=(−3,∞), R_(f⁻¹)=ℝ.'])
add(3,'H6','modelling','Reverse discrete model','Pemodelan diskret balik',
'P(t)=320bᵗ and P(3)=625. Find b, the percentage growth rate and P(5).',
'P(t)=320bᵗ dan P(3)=625. Tentukan b, persentase pertumbuhan, dan P(5).',
['625=320b³ → b³=125/64=(5/4)³.','The positive base is b=5/4=1.25, giving 25% growth per period.','P(5)=320(5/4)⁵=976.5625.'],
['625=320b³ → b³=125/64=(5/4)³.','Basis positifnya b=5/4=1.25, memberi pertumbuhan 25% per periode.','P(5)=320(5/4)⁵=976.5625.'])
add(3,'H7','modelling','When do models meet?','Kapan dua model bertemu?',
'A(t)=300(1.04)ᵗ and B(t)=250(1.08)ᵗ. Find when they are equal, in exact logarithmic form and numerically. Interpret the result.',
'A(t)=300(1.04)ᵗ dan B(t)=250(1.08)ᵗ. Tentukan kapan nilainya sama dalam bentuk log tepat dan numerik. Tafsirkan hasilnya.',
['Equating gives 300/250=(1.08/1.04)ᵗ, so 1.2=(1.08/1.04)ᵗ.','t=ln1.2/ln(1.08/1.04)≈4.83 time units.','The model curves meet at that real-valued time. If observations are only at integer periods, it is not an equality at an integer period.'],
['Menyamakan memberi 300/250=(1.08/1.04)ᵗ, sehingga 1.2=(1.08/1.04)ᵗ.','t=ln1.2/ln(1.08/1.04)≈4.83 satuan waktu.','Kurva model bertemu pada waktu real tersebut. Jika pengamatan hanya pada periode bulat, ini bukan kesamaan pada periode bulat.'])
add(3,'H8','equations','Decay inequality','Pertidaksamaan peluruhan',
'Solve 5(0.6)ˣ≤1. Give an exact logarithmic boundary and decimal approximation.',
'Selesaikan 5(0.6)ˣ≤1. Berikan batas logaritmik tepat dan pendekatan desimal.',
['Isolate: (0.6)ˣ≤0.2. Take logs: x ln0.6≤ln0.2.','Since ln0.6<0, division reverses the inequality.','x≥ln0.2/ln0.6≈3.15.'],
['Isolasi: (0.6)ˣ≤0.2. Ambil log: x ln0.6≤ln0.2.','Karena ln0.6<0, pembagian membalik arah pertidaksamaan.','x≥ln0.2/ln0.6≈3.15.'])
add(3,'H9','exponential','Reconstruct an exponential','Rekonstruksi eksponen',
'f(x)=Abˣ+1, A>0,b>0,b≠1, contains (0,4) and (2,13). Find A,b,f, its horizontal asymptote and range.',
'f(x)=Abˣ+1, A>0,b>0,b≠1, melalui (0,4) dan (2,13). Tentukan A,b,f, asimtot horizontal, dan range.',
['f(0)=4 → A+1=4 → A=3.','f(2)=13 → 3b²+1=13 → b²=4. Since b>0, b=2.','f(x)=3·2ˣ+1; asymptote y=1; range (1,∞).'],
['f(0)=4 → A+1=4 → A=3.','f(2)=13 → 3b²+1=13 → b²=4. Karena b>0, b=2.','f(x)=3·2ˣ+1; asimtot y=1; range (1,∞).'])
add(3,'H10','logarithm','Change of base','Ganti basis',
'Solve log₂x+log₄x=6 exactly.','Selesaikan log₂x+log₄x=6 secara tepat.',
['The original domain is x>0. Let u=log₂x; change of base gives log₄x=u/2.','u+u/2=6 → (3/2)u=6 → u=4.','log₂x=4 → x=16, which meets the domain.'],
['Domain awal x>0. Ambil u=log₂x; ganti basis memberi log₄x=u/2.','u+u/2=6 → (3/2)u=6 → u=4.','log₂x=4 → x=16, memenuhi domain.'])
add(3,'A1','equations','Non-routine substitution','Substitusi nonrutin',
'Solve 2(9ˣ)−7(3ˣ)+3=0. Give every exact real solution.',
'Selesaikan 2(9ˣ)−7(3ˣ)+3=0. Berikan semua solusi real tepat.',
['Set u=3ˣ>0; then 2u²−7u+3=0.','Factor: (2u−1)(u−3)=0 → u=1/2 or 3. Both are positive.','3ˣ=1/2 → x=−ln2/ln3; 3ˣ=3 → x=1.'],
['Ambil u=3ˣ>0; maka 2u²−7u+3=0.','Faktorkan: (2u−1)(u−3)=0 → u=1/2 atau 3. Keduanya positif.','3ˣ=1/2 → x=−ln2/ln3; 3ˣ=3 → x=1.'])
add(3,'A2','logarithm','Parameter and log solution counts','Parameter dan jumlah solusi log',
'For k>0, consider ln(x−1)+ln(5−x)=ln k. Count distinct real solutions for (a) 0<k<4, (b) k=4, (c) k>4. Explain the role of the logarithmic domain.',
'Untuk k>0, tinjau ln(x−1)+ln(5−x)=ln k. Hitung solusi real berbeda untuk (a) 0<k<4, (b) k=4, (c) k>4. Jelaskan peran domain log.',
['Require x>1 and x<5: domain 1<x<5.','Combine to obtain (x−1)(5−x)=k=4−(x−3)².','For 0<k<4 there are 2 roots; k=4 gives 1 root x=3; k>4 gives 0.','The endpoints 1 and 5 are excluded because a log argument becomes zero.'],
['Syarat x>1 dan x<5: domain 1<x<5.','Gabungkan menjadi (x−1)(5−x)=k=4−(x−3)².','Untuk 0<k<4 ada 2 akar; k=4 memberi 1 akar x=3; k>4 memberi 0.','Ujung 1 dan 5 dikeluarkan karena salah satu argumen log menjadi nol.'],'log-count')
add(3,'A3','equations','Exponential inequality by substitution','Pertidaksamaan eksponen via substitusi',
'Solve 2(4ˣ)−5(2ˣ)+2≤0.','Selesaikan 2(4ˣ)−5(2ˣ)+2≤0.',
['Set u=2ˣ>0; then 2u²−5u+2=(2u−1)(u−2)≤0.','The upward quadratic is nonpositive for 1/2≤u≤2.','Thus 2⁻¹≤2ˣ≤2¹. Since base 2 increases, −1≤x≤1.'],
['Ambil u=2ˣ>0; maka 2u²−5u+2=(2u−1)(u−2)≤0.','Kuadrat terbuka ke atas nonpositif untuk 1/2≤u≤2.','Jadi 2⁻¹≤2ˣ≤2¹. Karena basis 2 naik, −1≤x≤1.'])
add(3,'A4','modelling','Continuous-model reconstruction','Rekonstruksi model kontinu',
'P(t)=P₀e^(kt), P(2)=150, P(5)=240. Find exact k and P₀, numerical values, and the doubling time.',
'P(t)=P₀e^(kt), P(2)=150, P(5)=240. Tentukan k dan P₀ tepat, nilai numerik, dan waktu penggandaan.',
['Divide observations: 240/150=e^(3k)=8/5, so k=(1/3)ln(8/5)≈0.1567 per time unit.','P₀=150e^(−2k)=150(8/5)^(−2/3)≈109.7.','For doubling, e^(kT)=2, so T=ln2/k=3ln2/ln(8/5)≈4.42 time units.'],
['Bagi pengamatan: 240/150=e^(3k)=8/5, sehingga k=(1/3)ln(8/5)≈0.1567 per satuan waktu.','P₀=150e^(−2k)=150(8/5)^(−2/3)≈109.7.','Untuk penggandaan, e^(kT)=2, maka T=ln2/k=3ln2/ln(8/5)≈4.42 satuan waktu.'])
add(3,'A5','linearisation','Exponential linearisation','Linearisasi eksponen',
'y=kaˣ. A graph of ln y against x contains (1,ln18) and (3,ln162). Find its gradient, a,k and the original relationship.',
'y=kaˣ. Grafik ln y terhadap x melalui (1,ln18) dan (3,ln162). Tentukan gradien, a,k, dan hubungan asal.',
['ln y=ln k+x ln a. The gradient is (ln162−ln18)/(3−1)=ln9/2=ln3.','Thus ln a=ln3 → a=3. At x=1: ln18=ln k+ln3 → k=6.','The original relationship is y=6·3ˣ. Check: y(1)=18 and y(3)=162.'],
['ln y=ln k+x ln a. Gradien (ln162−ln18)/(3−1)=ln9/2=ln3.','Jadi ln a=ln3 → a=3. Pada x=1: ln18=ln k+ln3 → k=6.','Hubungan asal y=6·3ˣ. Cek: y(1)=18 dan y(3)=162.'],'linearisation')
add(3,'A6','inverse','Reconstruct from the inverse','Rekonstruksi dari invers',
'f⁻¹(x)=2ln((x−1)/3) and f(x)=Ae^(kx)+c. Find A,k,c and the domain/range of both functions.',
'f⁻¹(x)=2ln((x−1)/3) dan f(x)=Ae^(kx)+c. Tentukan A,k,c dan domain/range kedua fungsi.',
['Let y=2ln((x−1)/3). Then e^(y/2)=(x−1)/3 → x=3e^(y/2)+1.','Swap variables: f(x)=3e^(x/2)+1, so A=3,k=1/2,c=1.','D_f=ℝ,R_f=(1,∞); D_(f⁻¹)=(1,∞),R_(f⁻¹)=ℝ.'],
['Ambil y=2ln((x−1)/3). Maka e^(y/2)=(x−1)/3 → x=3e^(y/2)+1.','Tukar variabel: f(x)=3e^(x/2)+1, sehingga A=3,k=1/2,c=1.','D_f=ℝ,R_f=(1,∞); D_(f⁻¹)=(1,∞),R_(f⁻¹)=ℝ.'])
add(3,'A7','modelling','Reverse model comparison','Perbandingan model balik',
'A(t)=100bᵗ, B(t)=400(0.8)ᵗ, equal at t=4. Find exact b, the percentage growth rate of A, which is larger at t=0, and interpret the intersection.',
'A(t)=100bᵗ, B(t)=400(0.8)ᵗ, sama saat t=4. Tentukan b tepat, persentase pertumbuhan A, model yang lebih besar saat t=0, dan arti perpotongan.',
['100b⁴=400(0.8)⁴ → b⁴=4(0.8)⁴.','The positive base is b=0.8√2=4√2/5≈1.13137.','Growth rate =100(b−1)%≈13.1%. At t=0, B(0)=400>A(0)=100.','At t=4 the two quantities agree; the growing A catches the decaying B.'],
['100b⁴=400(0.8)⁴ → b⁴=4(0.8)⁴.','Basis positif b=0.8√2=4√2/5≈1.13137.','Laju pertumbuhan =100(b−1)%≈13.1%. Saat t=0, B(0)=400>A(0)=100.','Pada t=4 kedua kuantitas sama; A yang tumbuh menyusul B yang meluruh.'])
add(3,'A8','inverse','Transformed log and inverse','Log tertransformasi dan invers',
'For g(x)=2ln(3x−6)+4, find its domain, vertical asymptote, exact x-intercept, g⁻¹(x), and inverse domain/range.',
'Untuk g(x)=2ln(3x−6)+4, tentukan domain, asimtot vertikal, intersep-x tepat, g⁻¹(x), dan domain/range invers.',
['3x−6>0 → x>2; the vertical asymptote is x=2.','At g=0: ln(3x−6)=−2 → x=2+e⁻²/3; intercept (2+e⁻²/3,0).','y−4=2ln(3x−6) → x=2+(1/3)e^((y−4)/2).','g⁻¹(x)=2+(1/3)e^((x−4)/2); its domain is ℝ and range (2,∞).'],
['3x−6>0 → x>2; asimtot vertikal x=2.','Saat g=0: ln(3x−6)=−2 → x=2+e⁻²/3; intersep (2+e⁻²/3,0).','y−4=2ln(3x−6) → x=2+(1/3)e^((y−4)/2).','g⁻¹(x)=2+(1/3)e^((x−4)/2); domain ℝ dan range (2,∞).'])
add(3,'A9','equations','Parameterised exponential equation','Persamaan eksponen berparameter',
'For e^(2x)−(k+1)eˣ+k=0, find all k giving (a) two distinct real solutions, (b) exactly one. Explain why positivity matters.',
'Untuk e^(2x)−(k+1)eˣ+k=0, tentukan semua k yang memberi (a) dua solusi real berbeda, (b) tepat satu. Jelaskan pentingnya positivitas.',
['Set u=eˣ>0. Then u²−(k+1)u+k=(u−1)(u−k)=0.','u=1 always gives x=0. The root u=k gives real x=ln k only if k>0.','Two distinct solutions: k>0,k≠1. Exactly one: k≤0 or k=1.','At k=1 the two algebraic factors coincide, giving one distinct input. Nonpositive u cannot equal eˣ.'],
['Ambil u=eˣ>0. Maka u²−(k+1)u+k=(u−1)(u−k)=0.','u=1 selalu memberi x=0. Akar u=k memberi x=ln k real hanya jika k>0.','Dua solusi berbeda: k>0,k≠1. Tepat satu: k≤0 atau k=1.','Pada k=1 kedua faktor aljabar sama, memberi satu input berbeda. u nonpositif tidak mungkin sama dengan eˣ.'])
add(3,'A10','linearisation','Power-law linearisation','Linearisasi hukum pangkat',
'y=kxⁿ with x,y>0. A graph of ln y against ln x contains (0,ln3) and (ln4,ln24). Find n,k, the original relationship and y at x=9.',
'y=kxⁿ dengan x,y>0. Grafik ln y terhadap ln x melalui (0,ln3) dan (ln4,ln24). Tentukan n,k, hubungan asal, dan y saat x=9.',
['ln y=ln k+n ln x. The gradient n=(ln24−ln3)/ln4=ln8/ln4=3/2.','The intercept is ln3, so k=3; y=3x^(3/2).','At x=9, y=3·9^(3/2)=3·27=81.'],
['ln y=ln k+n ln x. Gradien n=(ln24−ln3)/ln4=ln8/ln4=3/2.','Intersep ln3, sehingga k=3; y=3x^(3/2).','Pada x=9, y=3·9^(3/2)=3·27=81.'],'power-line')
# Explicitly supply the continuity assumption required for the source's full-interval range.
q=next(q for q in questions if q['id']=='FG1-A7')
q['prompt']['en']=q['prompt']['en'].replace('A strictly increasing f','A continuous, strictly increasing f')
q['prompt']['id']=q['prompt']['id'].replace('Fungsi naik tegas f','Fungsi kontinu dan naik tegas f')
q['clarification']={'en':'Continuity is stated explicitly here: the PDF’s full-interval range needs this assumption; strict increase and endpoint extrema alone do not rule out jumps.','id':'Kontinuitas dinyatakan eksplisit di sini: range berupa interval penuh pada PDF memerlukan asumsi ini; naik tegas dan ekstrem ujung saja belum meniadakan lompatan.'}
Path(__file__).resolve().parents[1].joinpath('dist/bank.json').write_text(json.dumps(questions,ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(questions)} source-mapped bilingual questions.')
