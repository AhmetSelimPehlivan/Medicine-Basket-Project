----

CREATE TABLE public.aktiviteler (
    aktiviteid integer NOT NULL,
    aktivitetanimi character varying(255) NOT NULL
);


ALTER TABLE public.aktiviteler OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 17092)
-- Name: alanlar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alanlar (
    alanid integer NOT NULL,
    alanadi character varying(255) NOT NULL,
    alantipi character varying(250)
);


ALTER TABLE public.alanlar OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 17126)
-- Name: belirtecler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.belirtecler (
    belirtecid integer NOT NULL,
    belirtectanimi character varying(250) NOT NULL
);


ALTER TABLE public.belirtecler OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 17160)
-- Name: calisanproblem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.calisanproblem (
    problemid integer NOT NULL,
    kullaniciadi integer NOT NULL,
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    mudaheleid integer NOT NULL,
    aktiviteid integer NOT NULL,
    "aktiviteaciklama" character varying(250) NOT NULL,
    tarihi date NOT NULL
);


ALTER TABLE public.calisanproblem OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 17121)
-- Name: cikti; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cikti (
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    ciktiid integer NOT NULL,
    ciktiadi character varying(250) NOT NULL
);


ALTER TABLE public.cikti OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17131)
-- Name: ciktidetay; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ciktidetay (
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    ciktiid integer NOT NULL,
    belirtecid integer NOT NULL,
    sira integer
);


ALTER TABLE public.ciktidetay OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16622)
-- Name: eczaci; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eczaci (
    tcno numeric(14,0) NOT NULL,
    isim character varying(25) NOT NULL,
    telefon numeric(14,0) NOT NULL,
    adminparola character varying(25) NOT NULL,
    email text,
    eczane_id integer
);


ALTER TABLE public.eczaci OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16529)
-- Name: eczane; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eczane (
    eczane_id integer NOT NULL,
    isim character varying(25) NOT NULL,
    adres text NOT NULL,
    calismasaati time without time zone NOT NULL,
    sehir character varying(25) NOT NULL,
    parola character varying(20) NOT NULL
);


ALTER TABLE public.eczane OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16557)
-- Name: eczanecalisani; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eczanecalisani (
    tcno numeric(14,0) NOT NULL,
    isim character varying(25) NOT NULL,
    email character varying(50) NOT NULL,
    telefon numeric(14,0) NOT NULL,
    eczane_id integer NOT NULL,
    sifre character varying(25),
    status integer
);


ALTER TABLE public.eczanecalisani OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16941)
-- Name: eczaneilacbulunur; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eczaneilacbulunur (
    eczane_id integer NOT NULL,
    ilacadi character varying(25) NOT NULL
);


ALTER TABLE public.eczaneilacbulunur OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16961)
-- Name: eczaneilacsaglar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eczaneilacsaglar (
    eczane_id integer NOT NULL,
    kullanicitc integer NOT NULL,
    kuryetcno integer NOT NULL,
    saat time without time zone NOT NULL,
    gun date NOT NULL
);


ALTER TABLE public.eczaneilacsaglar OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16909)
-- Name: enabizverileri; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enabizverileri (
    tcno numeric(250,0) NOT NULL,
    receteno integer NOT NULL,
    ilacadi character varying(25) NOT NULL
);


ALTER TABLE public.enabizverileri OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 17190)
-- Name: ilacbilgi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ilacbilgi (
    ilacadi character varying(250) NOT NULL,
    fiyat integer NOT NULL
);


ALTER TABLE public.ilacbilgi OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 17150)
-- Name: ilaveciktidetay; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ilaveciktidetay (
    problemid integer NOT NULL,
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    mudahaleid integer NOT NULL,
    belirtecid integer NOT NULL,
    sira integer NOT NULL,
    ekleyenkullaniciadi character varying(250) NOT NULL,
    eklenmetarihi date NOT NULL
);


ALTER TABLE public.ilaveciktidetay OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 17147)
-- Name: ilavemudahaledetay; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ilavemudahaledetay (
    problemid integer NOT NULL,
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    mudahaleid integer NOT NULL,
    aktiviteid integer NOT NULL,
    sira integer NOT NULL,
    ekleyenkullaniciadi character varying(250) NOT NULL,
    eklenmetarihi date NOT NULL
);


ALTER TABLE public.ilavemudahaledetay OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16923)
-- Name: kullanici; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kullanici (
    tcno numeric(14,0) NOT NULL,
    isim character varying(250) NOT NULL,
    telefon character varying(250) NOT NULL,
    sifre character varying(250),
    sehir character varying(250),
    adres character varying(250),
    email character varying(250)
);


ALTER TABLE public.kullanici OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16787)
-- Name: kurye; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kurye (
    tcno integer NOT NULL,
    isim character varying(25) NOT NULL,
    telefon character varying(25) NOT NULL,
    maas integer NOT NULL,
    email character varying(25) NOT NULL,
    eczane_id integer NOT NULL
);


ALTER TABLE public.kurye OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 17106)
-- Name: mudahale; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mudahale (
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    mudahaleid integer NOT NULL,
    mudahaleadi character varying(255) NOT NULL
);


ALTER TABLE public.mudahale OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17116)
-- Name: mudahaledetay; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mudahaledetay (
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    mudahaleid integer NOT NULL,
    aktiviteid integer NOT NULL,
    sira integer NOT NULL
);


ALTER TABLE public.mudahaledetay OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 17153)
-- Name: personelproblem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.personelproblem (
    problemid integer NOT NULL,
    kullaniciadi character varying(250) NOT NULL
);


ALTER TABLE public.personelproblem OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 17209)
-- Name: problem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problem (
    problemtipiid integer NOT NULL,
    problemtanimi character varying(255) NOT NULL,
    problemitanimlayiciismi character varying(255),
    problemitanimlayantcno character varying(255) NOT NULL,
    hedeflenenamactanimi text NOT NULL
);


ALTER TABLE public.problem OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 17136)
-- Name: problembirim; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problembirim (
    problemid integer NOT NULL,
    birimid integer NOT NULL,
    eslenmetarihi date
);


ALTER TABLE public.problembirim OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17144)
-- Name: problemcikti; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problemcikti (
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    ciktiid integer NOT NULL,
    problemid integer NOT NULL
);


ALTER TABLE public.problemcikti OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 17156)
-- Name: problemciktidegerlendirme; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problemciktidegerlendirme (
    problemid integer NOT NULL,
    belirtecid integer NOT NULL,
    skor integer NOT NULL,
    skortarihi date NOT NULL
);


ALTER TABLE public.problemciktidegerlendirme OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 17163)
-- Name: problemdurumdegerlendirme; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problemdurumdegerlendirme (
    problemid integer NOT NULL,
    yeniproblemid integer NOT NULL,
    "yeniproblemtanımı" character varying(250) NOT NULL,
    yenihedef character varying(250) NOT NULL,
    oncekiproblemskoru integer NOT NULL,
    tahminedilenproblemskoru integer NOT NULL,
    degerlendirmetarihi date NOT NULL,
    degerlendirenkullaniciadi character varying(250) NOT NULL
);


ALTER TABLE public.problemdurumdegerlendirme OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 17141)
-- Name: problemmudahale; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problemmudahale (
    alanid integer NOT NULL,
    sinifid integer NOT NULL,
    mudahaleid integer NOT NULL,
    problemid integer NOT NULL
);


ALTER TABLE public.problemmudahale OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 17099)
-- Name: siniflar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.siniflar (
    sinifid integer NOT NULL,
    sinifadi character varying(255) NOT NULL,
    alantipi character varying(250)
);


ALTER TABLE public.siniflar OWNER TO postgres;

--
-- TOC entry 3290 (class 2606 OID 17115)
-- Name: aktiviteler aktiviteler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aktiviteler
    ADD CONSTRAINT aktiviteler_pkey PRIMARY KEY (aktivitetanimi);


--
-- TOC entry 3286 (class 2606 OID 17098)
-- Name: alanlar alanlar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alanlar
    ADD CONSTRAINT alanlar_pkey PRIMARY KEY (alanid);


--
-- TOC entry 3296 (class 2606 OID 17130)
-- Name: belirtecler belirtecler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.belirtecler
    ADD CONSTRAINT belirtecler_pkey PRIMARY KEY (belirtecid);


--
-- TOC entry 3294 (class 2606 OID 17125)
-- Name: cikti cikti_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cikti
    ADD CONSTRAINT cikti_pkey PRIMARY KEY (alanid, sinifid, ciktiid);


--
-- TOC entry 3298 (class 2606 OID 17135)
-- Name: ciktidetay ciktidetay_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciktidetay
    ADD CONSTRAINT ciktidetay_pkey PRIMARY KEY (alanid, sinifid, ciktiid, belirtecid);


--
-- TOC entry 3272 (class 2606 OID 17252)
-- Name: eczaci eczacı_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczaci
    ADD CONSTRAINT "eczacı_pkey" PRIMARY KEY (tcno);


--
-- TOC entry 3268 (class 2606 OID 16535)
-- Name: eczane eczane_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczane
    ADD CONSTRAINT eczane_pkey PRIMARY KEY (eczane_id);


--
-- TOC entry 3270 (class 2606 OID 17234)
-- Name: eczanecalisani eczanecalisani_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczanecalisani
    ADD CONSTRAINT eczanecalisani_pkey PRIMARY KEY (tcno);


--
-- TOC entry 3282 (class 2606 OID 16945)
-- Name: eczaneilacbulunur eczaneilacbulunur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczaneilacbulunur
    ADD CONSTRAINT eczaneilacbulunur_pkey PRIMARY KEY (eczane_id, ilacadi);


--
-- TOC entry 3284 (class 2606 OID 16965)
-- Name: eczaneilacsaglar eczaneilacsaglar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczaneilacsaglar
    ADD CONSTRAINT eczaneilacsaglar_pkey PRIMARY KEY (eczane_id, kullanicitc, kuryetcno);


--
-- TOC entry 3276 (class 2606 OID 17245)
-- Name: enabizverileri enabizverileri_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enabizverileri
    ADD CONSTRAINT enabizverileri_pkey PRIMARY KEY (receteno, tcno);


--
-- TOC entry 3278 (class 2606 OID 16915)
-- Name: enabizverileri enabizverileri_receteno_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enabizverileri
    ADD CONSTRAINT enabizverileri_receteno_key UNIQUE (receteno);


--
-- TOC entry 3304 (class 2606 OID 17196)
-- Name: ilacbilgi ilacbilgi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ilacbilgi
    ADD CONSTRAINT ilacbilgi_pkey PRIMARY KEY (ilacadi);


--
-- TOC entry 3280 (class 2606 OID 17221)
-- Name: kullanici kullanici_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kullanici
    ADD CONSTRAINT kullanici_pkey PRIMARY KEY (tcno);


--
-- TOC entry 3274 (class 2606 OID 16791)
-- Name: kurye kurye_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kurye
    ADD CONSTRAINT kurye_pkey PRIMARY KEY (tcno);


--
-- TOC entry 3288 (class 2606 OID 17110)
-- Name: mudahale mudahale_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mudahale
    ADD CONSTRAINT mudahale_pkey PRIMARY KEY (alanid, sinifid, mudahaleid);


--
-- TOC entry 3292 (class 2606 OID 17120)
-- Name: mudahaledetay mudahaledetay_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mudahaledetay
    ADD CONSTRAINT mudahaledetay_pkey PRIMARY KEY (alanid, sinifid, mudahaleid, aktiviteid);


--
-- TOC entry 3300 (class 2606 OID 17140)
-- Name: problembirim problembirim_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problembirim
    ADD CONSTRAINT problembirim_pkey PRIMARY KEY (problemid, birimid);


--
-- TOC entry 3302 (class 2606 OID 17169)
-- Name: problemdurumdegerlendirme problemdurumdegerlendirme_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problemdurumdegerlendirme
    ADD CONSTRAINT problemdurumdegerlendirme_pkey PRIMARY KEY (problemid, yeniproblemid);


--
-- TOC entry 3305 (class 2606 OID 16562)
-- Name: eczanecalisani eczanecalisani_eczane_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczanecalisani
    ADD CONSTRAINT eczanecalisani_eczane_id_fkey FOREIGN KEY (eczane_id) REFERENCES public.eczane(eczane_id);


--
-- TOC entry 3308 (class 2606 OID 16966)
-- Name: eczaneilacsaglar eczaneilacsaglar_eczane_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczaneilacsaglar
    ADD CONSTRAINT eczaneilacsaglar_eczane_id_fkey FOREIGN KEY (eczane_id) REFERENCES public.eczane(eczane_id);


--
-- TOC entry 3307 (class 2606 OID 17222)
-- Name: eczaneilacsaglar eczaneilacsaglar_kullanicitc_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczaneilacsaglar
    ADD CONSTRAINT eczaneilacsaglar_kullanicitc_fkey FOREIGN KEY (kullanicitc) REFERENCES public.kullanici(tcno);


--
-- TOC entry 3309 (class 2606 OID 16976)
-- Name: eczaneilacsaglar eczaneilacsaglar_kuryetcno_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eczaneilacsaglar
    ADD CONSTRAINT eczaneilacsaglar_kuryetcno_fkey FOREIGN KEY (kuryetcno) REFERENCES public.kurye(tcno);


--
-- TOC entry 3306 (class 2606 OID 16792)
-- Name: kurye kurye_eczane_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kurye
    ADD CONSTRAINT kurye_eczane_id_fkey FOREIGN KEY (eczane_id) REFERENCES public.eczane(eczane_id);


-- Completed on 2021-11-24 22:30:47

--
-- PostgreSQL database dump complete
--

