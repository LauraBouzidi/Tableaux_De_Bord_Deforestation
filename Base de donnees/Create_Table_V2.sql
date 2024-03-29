USE [master]
GO
/****** Object:  User [##MS_PolicyEventProcessingLogin##]    Script Date: 21/03/2019 13:00:41 ******/
CREATE USER [##MS_PolicyEventProcessingLogin##] FOR LOGIN [##MS_PolicyEventProcessingLogin##] WITH DEFAULT_SCHEMA=[dbo]
GO
/****** Object:  User [##MS_AgentSigningCertificate##]    Script Date: 21/03/2019 13:00:41 ******/
CREATE USER [##MS_AgentSigningCertificate##] FOR LOGIN [##MS_AgentSigningCertificate##]
GO
/****** Object:  Table [dbo].[Articles]    Script Date: 21/03/2019 13:00:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Articles](
	[Id_article] [varchar](50) NOT NULL,
	[Titre] [varchar](5000) NULL,
	[date_article] [int] NULL,
	[sentiment] [float] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Auteurs]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Auteurs](
	[Id_auteur] [int] NOT NULL,
	[nom_auteur] [varchar](200) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Comporte]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Comporte](
	[Id_article] [varchar](50) NOT NULL,
	[Id_mot] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Concerne]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Concerne](
	[Id_article] [varchar](50) NOT NULL,
	[Id_pays] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Ecrit]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Ecrit](
	[Id_article] [varchar](50) NOT NULL,
	[Id_auteur] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Mot_clefs]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Mot_clefs](
	[Id_mot] [int] NOT NULL,
	[mot] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Origine]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Origine](
	[Id_article] [varchar](50) NOT NULL,
	[Id_pays] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Pays]    Script Date: 21/03/2019 13:00:42 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Pays](
	[Id_pays] [int] NOT NULL,
	[nom_pays] [varchar](50) NULL
) ON [PRIMARY]
GO
