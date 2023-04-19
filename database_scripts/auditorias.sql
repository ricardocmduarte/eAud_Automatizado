-- Table: public.auditorias

-- DROP TABLE IF EXISTS public.auditorias;

CREATE TABLE IF NOT EXISTS public.auditorias
(
    id integer NOT NULL,
    situacao character varying(255) COLLATE pg_catalog."default",
    estado character varying(255) COLLATE pg_catalog."default",
    atividade character varying(255) COLLATE pg_catalog."default",
    titulo character varying(1000) COLLATE pg_catalog."default",
    idtarefaassociada integer,
    titulotarefaassociada character varying(500) COLLATE pg_catalog."default",
    dtprevisaoinicio character varying(50) COLLATE pg_catalog."default",
    dtprevisaofim character varying(50) COLLATE pg_catalog."default",
    dtrealizadainicio character varying(50) COLLATE pg_catalog."default",
    dtrealizadafim character varying(50) COLLATE pg_catalog."default",
    prioridade character varying(255) COLLATE pg_catalog."default",
    assunto character varying(5000) COLLATE pg_catalog."default",
    idatividade integer,
    descricaoatividade character varying(5000) COLLATE pg_catalog."default",
    idsituacao integer,
    dataultimamodificacao character varying(50) COLLATE pg_catalog."default",
    autorultimamodificacao character varying(500) COLLATE pg_catalog."default",
    objetosauditoria character varying(5000) COLLATE pg_catalog."default",
    processosassociados character varying(5000) COLLATE pg_catalog."default",
    dadosgerenciais character varying(5000) COLLATE pg_catalog."default",
    gerentesauditoria character varying(5000) COLLATE pg_catalog."default",
    relatoriopreliminar character varying(5000) COLLATE pg_catalog."default",
    proponenteauditoria character varying(5000) COLLATE pg_catalog."default",
    duracaomeses integer,
    recursofinanceiro character varying(5000) COLLATE pg_catalog."default",
    conhecimentostecnicos character varying(5000) COLLATE pg_catalog."default",
    localidadesauditoria character varying(5000) COLLATE pg_catalog."default",
    responsavelauditoria character varying(5000) COLLATE pg_catalog."default",
    anexorelatoripreliminar character varying(5000) COLLATE pg_catalog."default",
    resultadosesperados character varying(5000) COLLATE pg_catalog."default",
    resultadosindicador character varying(5000) COLLATE pg_catalog."default",
    resultadosdescricao character varying(5000) COLLATE pg_catalog."default",
    origemdemanda character varying(5000) COLLATE pg_catalog."default",
    pessoajuridica character varying(5000) COLLATE pg_catalog."default",
    tipoconsultoria character varying(5000) COLLATE pg_catalog."default",
    nundenuncia integer,
    unidadesauditadas character varying(5000) COLLATE pg_catalog."default",
    homemhoras integer,
    equipeauditoria character varying(5000) COLLATE pg_catalog."default",
    anexorel character varying(5000) COLLATE pg_catalog."default",
    areasrequeridas character varying(5000) COLLATE pg_catalog."default",
    objetivoauditoria character varying(5000) COLLATE pg_catalog."default",
    envolvidosauditoria character varying(5000) COLLATE pg_catalog."default",
    processotrabalhoauditoria character varying(5000) COLLATE pg_catalog."default",
    anexosauditoria character varying(5000) COLLATE pg_catalog."default",
    linhaacaoauditoria character varying(5000) COLLATE pg_catalog."default",
    relatoriofinal character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT auditorias_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auditorias
    OWNER to m1478769;

REVOKE ALL ON TABLE public.auditorias FROM x09972752;

GRANT SELECT ON TABLE public.auditorias TO m13365929;

GRANT ALL ON TABLE public.auditorias TO m1478769;

GRANT SELECT ON TABLE public.auditorias TO m7532203;

GRANT SELECT ON TABLE public.auditorias TO x09972752;
