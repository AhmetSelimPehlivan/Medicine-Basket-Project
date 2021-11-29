
-- Data for Name: aktiviteler; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.aktiviteler (aktiviteid, aktivitetanimi) VALUES (1, 'ilac Takviyesi');
INSERT INTO public.aktiviteler (aktiviteid, aktivitetanimi) VALUES (2, 'ilaclari Sisteme Gir');
INSERT INTO public.aktiviteler (aktiviteid, aktivitetanimi) VALUES (3, 'ilaclari duzenle');
INSERT INTO public.aktiviteler (aktiviteid, aktivitetanimi) VALUES (4, 'Kurye ile baglanti kur');
INSERT INTO public.aktiviteler (aktiviteid, aktivitetanimi) VALUES (5, 'Online Siparis Hazirla');


--
-- TOC entry 3457 (class 0 OID 17092)
-- Dependencies: 217
-- Data for Name: alanlar; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alanlar (alanid, alanadi, alantipi) VALUES (2, 'ilac Depo', '1');
INSERT INTO public.alanlar (alanid, alanadi, alantipi) VALUES (3, 'Kurye Birimi', '1');
INSERT INTO public.alanlar (alanid, alanadi, alantipi) VALUES (1, 'Eczane girisi', '1');
INSERT INTO public.alanlar (alanid, alanadi, alantipi) VALUES (4, 'Eczane Deposu', '2');


--
-- TOC entry 3463 (class 0 OID 17126)
-- Dependencies: 223
-- Data for Name: belirtecler; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.belirtecler (belirtecid, belirtectanimi) VALUES (4, 'ilac Dogru Kategoride Mi?');
INSERT INTO public.belirtecler (belirtecid, belirtectanimi) VALUES (5, 'ilac Paketlendi mi?');
INSERT INTO public.belirtecler (belirtecid, belirtectanimi) VALUES (2, 'ilac Kullaniciya ulasildi mi?');
INSERT INTO public.belirtecler (belirtecid, belirtectanimi) VALUES (1, 'ilac Kuryeye Verildi Mi?');
INSERT INTO public.belirtecler (belirtecid, belirtectanimi) VALUES (3, 'Hedef ilac sayisina Ulasildi mi?');


--
-- TOC entry 3472 (class 0 OID 17160)
-- Dependencies: 232
-- Data for Name: calisanproblem; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3462 (class 0 OID 17121)
-- Dependencies: 222
-- Data for Name: cikti; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cikti (alanid, sinifid, ciktiid, ciktiadi) VALUES (1, 1, 1, 'ilac Takviye Edildi');
INSERT INTO public.cikti (alanid, sinifid, ciktiid, ciktiadi) VALUES (1, 1, 2, 'ilaclar Sisteme Girildi');
INSERT INTO public.cikti (alanid, sinifid, ciktiid, ciktiadi) VALUES (3, 1, 1, 'Siparis Paketlendi');
INSERT INTO public.cikti (alanid, sinifid, ciktiid, ciktiadi) VALUES (1, 1, 3, 'ilac Satildi');


--
-- TOC entry 3464 (class 0 OID 17131)
-- Dependencies: 224
-- Data for Name: ciktidetay; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ciktidetay (alanid, sinifid, ciktiid, belirtecid, sira) VALUES (1, 1, 1, 1, 1);
INSERT INTO public.ciktidetay (alanid, sinifid, ciktiid, belirtecid, sira) VALUES (1, 1, 1, 4, 2);
INSERT INTO public.ciktidetay (alanid, sinifid, ciktiid, belirtecid, sira) VALUES (1, 1, 2, 4, 3);


--
-- TOC entry 3451 (class 0 OID 16622)
-- Dependencies: 211
-- Data for Name: eczaci; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.eczaci (tcno, isim, telefon, adminparola, email, eczane_id) VALUES (123123123, 'asdasdasd', 1231231, 'sdasdasdasd', 'asdasd@hotmail.com', NULL);
INSERT INTO public.eczaci (tcno, isim, telefon, adminparola, email, eczane_id) VALUES (12345678912, 'Ahmet Selim', 555555555, 'selimyucu03', 'ahmet@gmail.com', NULL);
INSERT INTO public.eczaci (tcno, isim, telefon, adminparola, email, eczane_id) VALUES (1223, 'Ahmet Selim', 5231, 'selimyucu03', 'selim@gmail.com', NULL);


--
-- TOC entry 3449 (class 0 OID 16529)
-- Dependencies: 209
-- Data for Name: eczane; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.eczane (eczane_id, isim, adres, calismasaati, sehir, parola) VALUES (123, 'busra eczanesi', 'guvenevler Mah', '13:30:00', 'Afyonkarahisar', '1');


--
-- TOC entry 3450 (class 0 OID 16557)
-- Dependencies: 210
-- Data for Name: eczanecalisani; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.eczanecalisani (tcno, isim, email, telefon, eczane_id, sifre, status) VALUES (1111111113, 'Mehmet atif', 'mehmet@gmail.com', 555242, 123, 'mehmetatif', 2);
INSERT INTO public.eczanecalisani (tcno, isim, email, telefon, eczane_id, sifre, status) VALUES (1111111112, 'Mehmet Selim', 'mehmetselim@gmail.com', 5342555565, 123, 'mehmetselim00', 1);
INSERT INTO public.eczanecalisani (tcno, isim, email, telefon, eczane_id, sifre, status) VALUES (1111111114, 'Selim', 'selim@gmail.com', 55454454, 123, 'selim03.', 2);


--
-- TOC entry 3455 (class 0 OID 16941)
-- Dependencies: 215
-- Data for Name: eczaneilacbulunur; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3456 (class 0 OID 16961)
-- Dependencies: 216
-- Data for Name: eczaneilacsaglar; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3453 (class 0 OID 16909)
-- Dependencies: 213
-- Data for Name: enabizverileri; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.enabizverileri (tcno, receteno, ilacadi) VALUES (12345678912, 1, 'Parol');
INSERT INTO public.enabizverileri (tcno, receteno, ilacadi) VALUES (12345678912, 2, 'Minoset');
INSERT INTO public.enabizverileri (tcno, receteno, ilacadi) VALUES (12345678912, 3, 'Agumentin');


--
-- TOC entry 3474 (class 0 OID 17190)
-- Dependencies: 234
-- Data for Name: ilacbilgi; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ilacbilgi (ilacadi, fiyat) VALUES ('Parol', 10);
INSERT INTO public.ilacbilgi (ilacadi, fiyat) VALUES ('Minoset', 11);
INSERT INTO public.ilacbilgi (ilacadi, fiyat) VALUES ('Agumentin', 18);


--
-- TOC entry 3469 (class 0 OID 17150)
-- Dependencies: 229
-- Data for Name: ilaveciktidetay; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3468 (class 0 OID 17147)
-- Dependencies: 228
-- Data for Name: ilavemudahaledetay; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3454 (class 0 OID 16923)
-- Dependencies: 214
-- Data for Name: kullanici; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (1320505, 'ahmet', '5342516612', 's', NULL, NULL, 'ahmetseil.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (213123, 'asdasd', '2e123', '5', NULL, NULL, 'asdasd@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (12312, '23232', '2323', 'a', NULL, NULL, 'asdasl.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (123, 'Ahmet Selim', '123', '1', NULL, NULL, 'asdas@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (123323, 'Ahmet Selim', '123', '2', NULL, NULL, 'asdas@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (5646, 'asda', '5465', '5', NULL, NULL, '2asd@gmaik.cpm');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (121244, 'Sefa yigit', '545412', '1', NULL, NULL, 'asdas@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (181101033, 'Ahmet Pehlivan', '55555', 's', NULL, NULL, 'ahmet@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (181101032, 'Ahmet Pehlivan', '535555', 's', NULL, NULL, 'selimpehlivan@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (181101010, 'Ahmet Selim', '555555', 's', NULL, NULL, 'ahmet@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (181101005, 'Ahmet Pehlivan', '555555', 'S', NULL, NULL, 'ahmet@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (181101002, 'Ahmet Pehlivan', '555555', 's', NULL, NULL, 'ahmet@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (181101001, 'Ahmet Selim', '555555', 's', NULL, NULL, 'ahmet@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (213123123, 'asdasd', '23123', 's', NULL, NULL, 'qadsd@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (2122223123, 'asdasd', '23123', 'sddsd', NULL, NULL, 'qadsd@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (13207422154, 'Ahmet Selim', '555555555', 'selimyucu03', NULL, NULL, 'ahmetpqhlivan@gmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (1325545754, 'Ahmet Selim', '555555555', 'selimyucu03.', NULL, NULL, 'ahmetpehlivan@hotmail.com');
INSERT INTO public.kullanici (tcno, isim, telefon, sifre, sehir, adres, email) VALUES (12345678912, 'Ahmet Selim', '55555555555', 'selimyucu03', NULL, NULL, 'ahmet@gmail.com');


--
-- TOC entry 3452 (class 0 OID 16787)
-- Dependencies: 212
-- Data for Name: kurye; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3459 (class 0 OID 17106)
-- Dependencies: 219
-- Data for Name: mudahale; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (1, 1, 2, 'Sisteme ilac Girisi');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (1, 1, 3, 'ilac Satis');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (1, 1, 4, 'ilac Duzenleme');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (1, 1, 5, 'Son Kullanma Tarihi Kontrol');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (2, 1, 1, 'Takviye');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (2, 1, 2, 'ilac Duzenleme');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (2, 1, 3, 'ilac Satis');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (3, 1, 1, 'Siparis Paketleme');
INSERT INTO public.mudahale (alanid, sinifid, mudahaleid, mudahaleadi) VALUES (1, 1, 1, 'ilac Takviye');


--
-- TOC entry 3461 (class 0 OID 17116)
-- Dependencies: 221
-- Data for Name: mudahaledetay; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.mudahaledetay (alanid, sinifid, mudahaleid, aktiviteid, sira) VALUES (2, 1, 3, 4, 1);
INSERT INTO public.mudahaledetay (alanid, sinifid, mudahaleid, aktiviteid, sira) VALUES (1, 1, 1, 4, 2);
INSERT INTO public.mudahaledetay (alanid, sinifid, mudahaleid, aktiviteid, sira) VALUES (1, 1, 2, 4, 3);


--
-- TOC entry 3470 (class 0 OID 17153)
-- Dependencies: 230
-- Data for Name: personelproblem; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.personelproblem (problemid, kullaniciadi) VALUES (1, '123');
INSERT INTO public.personelproblem (problemid, kullaniciadi) VALUES (2, '123');
INSERT INTO public.personelproblem (problemid, kullaniciadi) VALUES (3, '1111111114');


--
-- TOC entry 3475 (class 0 OID 17209)
-- Dependencies: 235
-- Data for Name: problem; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.problem (problemtipiid, problemtanimi, problemitanimlayiciismi, problemitanimlayantcno, hedeflenenamactanimi) VALUES (1, 'ilac Ekle', 'Ahmet Selim', '1811101033', 'Envantere ilac Ekle');


--
-- TOC entry 3465 (class 0 OID 17136)
-- Dependencies: 225
-- Data for Name: problembirim; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.problembirim (problemid, birimid, eslenmetarihi) VALUES (1, 1, '2021-11-21');
INSERT INTO public.problembirim (problemid, birimid, eslenmetarihi) VALUES (2, 1, '2021-11-20');
INSERT INTO public.problembirim (problemid, birimid, eslenmetarihi) VALUES (1, 2, '2021-11-20');
INSERT INTO public.problembirim (problemid, birimid, eslenmetarihi) VALUES (2, 3, '2021-11-20');
INSERT INTO public.problembirim (problemid, birimid, eslenmetarihi) VALUES (3, 2, '2021-11-20');
INSERT INTO public.problembirim (problemid, birimid, eslenmetarihi) VALUES (3, 3, '2021-11-20');


--
-- TOC entry 3467 (class 0 OID 17144)
-- Dependencies: 227
-- Data for Name: problemcikti; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.problemcikti (alanid, sinifid, ciktiid, problemid) VALUES (1, 1, 1, 1);
INSERT INTO public.problemcikti (alanid, sinifid, ciktiid, problemid) VALUES (1, 1, 1, 2);
INSERT INTO public.problemcikti (alanid, sinifid, ciktiid, problemid) VALUES (1, 1, 1, 3);


--
-- TOC entry 3471 (class 0 OID 17156)
-- Dependencies: 231
-- Data for Name: problemciktidegerlendirme; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3473 (class 0 OID 17163)
-- Dependencies: 233
-- Data for Name: problemdurumdegerlendirme; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3466 (class 0 OID 17141)
-- Dependencies: 226
-- Data for Name: problemmudahale; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.problemmudahale (alanid, sinifid, mudahaleid, problemid) VALUES (1, 1, 1, 1);
INSERT INTO public.problemmudahale (alanid, sinifid, mudahaleid, problemid) VALUES (1, 1, 1, 2);
INSERT INTO public.problemmudahale (alanid, sinifid, mudahaleid, problemid) VALUES (1, 1, 1, 3);
INSERT INTO public.problemmudahale (alanid, sinifid, mudahaleid, problemid) VALUES (2, 2, 3, 4);
INSERT INTO public.problemmudahale (alanid, sinifid, mudahaleid, problemid) VALUES (2, 3, 2, 5);


--
-- TOC entry 3458 (class 0 OID 17099)
-- Dependencies: 218
-- Data for Name: siniflar; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.siniflar (sinifid, sinifadi, alantipi) VALUES (2, 'Mavi Receteli ilaclar', '2');
INSERT INTO public.siniflar (sinifid, sinifadi, alantipi) VALUES (3, 'agri Kesiciler', '2');
INSERT INTO public.siniflar (sinifid, sinifadi, alantipi) VALUES (4, 'Kirmizi Receteli ilaclar', '2');
INSERT INTO public.siniflar (sinifid, sinifadi, alantipi) VALUES (5, 'Yesil Receteli ilaclar', '5');
INSERT INTO public.siniflar (sinifid, sinifadi, alantipi) VALUES (1, 'Vitaminler', '2');
INSERT INTO public.siniflar (sinifid, sinifadi, alantipi) VALUES (6, 'Kremler', '2');


-- Completed on 2021-11-24 22:22:14

--
-- PostgreSQL database dump complete
--

