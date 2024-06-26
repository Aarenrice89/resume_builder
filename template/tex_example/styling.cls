% Created by Murat Can Karacabey
% inspired by Michael Pollind's Awesome CV
% this is inspired by Aaren Rice's CV
% Created from scratch as a much simpler alternative to it to actually learn LaTeX.
% Might be interpreted as an easier-to-edit or easier-to-understand-what-is-going-on version of it.
\author{Murat Can Karacabey & Aaren Rice}
\RequirePackage[dvipsnames]{xcolor} % moved here I guess article class causes option clash with xcolor if used after loading the class
\LoadClass[11pt]{article}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{styling}[2024/05/25 Rice CV Class]
\RequirePackage[sfdefault]{noto}
\RequirePackage{etoolbox}
\RequirePackage{pgffor}
\RequirePackage{titlesec}
\RequirePackage{tikz}
\RequirePackage{fontspec}
\RequirePackage[left=0.5in,top=0.1in,right=0.5in,bottom=0.1in]{geometry} % DOCUMENT MARGINS
\RequirePackage{hyperref}
\RequirePackage{fontawesome}
\RequirePackage{mfirstuc}
\RequirePackage{ifthen}
\RequirePackage{lipsum}
\RequirePackage{array}
\pagestyle{empty}

\usepackage{comment}
\usepackage{tabularx}
\usepackage[overlay,absolute]{textpos}

\let\clearpage\relax

%Setup
\newcommand*{\setname}[2]{\def\@firstname{#1}\def\@lastname{#2}}
\newcommand*{\setaddress}[1]{\def\@address{#1}}
\newcommand*{\setmobile}[1]{\def\@mobile{#1}}
\newcommand*{\setposition}[1]{\def\@position{#1}}
\newcommand*{\setmail}[1]{\def\@mail{#1}}
\newcommand*{\setcitizenship}[1]{\def\@citizenship{#1}}
\newcommand*{\setthemecolor}[1]{\def\@themecolor{#1}}
\newcommand*{\setlinkedinaccount}[1]{\def\@linkedinaccount{#1}}
\newcommand*{\setgithubaccount}[1]{\def\@githubaccount{#1}}
\newcommand*{\setyearsofexperience}[1]{\def\@yoe{#1}}
\newcommand*{\setpostingurl}[2]{\def\@jobtitle{#1}\def\@postingurl{#2}}

\hypersetup{
    colorlinks=true,
    urlcolor=NavyBlue,
}

\newcommand\headerview{
  \noindent\begin{tabularx}{\textwidth}{@{} X r @{}}
    \name & {
        \begin{tabular}[t]{@{} l}
          \vspace{-3mm} \\
          \githubview \\
          \linkedinview \\
        \end{tabular}
    } \\
    \vspace{-5mm}
    \begin{tabular}[t]{@{} l}
        \contactinfo \\
        \yearsofexperience \\
        \mail \\
    \end{tabular}
  \end{tabularx}
  \begin{textblock*}{20mm}(177mm,21.5mm)
    \postinglink
  \end{textblock*}
}

\newcommand{\linkedinview}{\href{\@linkedinaccount}{\faLinkedinSquare\ \footnotesize linkedin}}
\newcommand{\githubview}{\href{\@githubaccount}{\faGithub\ \footnotesize github}}
\newcommand{\postinglink}{\href{\@postingurl}{\color{gray} \faLink\ \footnotesize posting}}
\newcommand{\name}{{\LARGE \color{\@themecolor} \@firstname \ \@lastname}}
\newcommand{\contactinfo}{{\footnotesize \color{gray}{\faMapMarker\ \@address} \ \ {\faPhone\ \@mobile}}}

\newcommand{\yearsofexperience}{%
{\footnotesize \@yoe \ years of experience}
}

\newcommand{\mail}{%
  {\footnotesize \href{mailto:\@mail}{\@mail}}
}

% Helper commands
\newcommand\ruleafter[1]{#1~{\color{black!60!\@themecolor}\hrulefill}} % a trick to put the line with <before> parameter in \titleformat

%colorful pipe separator
\newcommand{\cps}{{\color{\@themecolor} \quad\textbar\quad}}
\newcommand{\cpshalf}{{\color{\@themecolor} \textbar\hspace{0.2em}}}
\newcommand{\coloredbullet}{{\color{\@themecolor} \textbullet}}

% Edit section styles
\titleformat{\section}      % Customise the \section command
  {\large\bfseries\scshape\raggedright\color{\@themecolor}} % Make the \section headers large (\Large),
                               % small capitals (\scshape) and left aligned (\raggedright)
  {}{0em}                      % Can be used to give a prefix to all sections, like 'Section ...'
  {\ruleafter}                           % Can be used to insert code before the heading

\titlespacing*{\section}{-1pt}{-10pt}{0pt}

% Textview commands
\newcommand{\experience}[2]{%
  \mbox { \hspace{1em} \scshape \textbf{#1} }%
}

\newcommand{\datetext}[1]{%
{\itshape  \footnotesize \mdseries  \color{black} #1 }
}

\newcommand{\datetextbold}[1]{%
{\footnotesize \mdseries  \color{black} \textbf{#1} }
}

\newcommand{\datedexperience}[2]{%
  \begin{small} \mbox { \hspace{1em} \textbf{#1} } \end{small} \hfill \datetextbold{#2}\\[0.01cm] %
}

\newcommand{\explanation}[2]{%
    \mbox { \hspace{1.2em} \footnotesize \emph{#1}} \hfill \datetext{#2}\\[0.01cm] %
}

\newcommand{\explanationdetail}[1]{%
    \indent \indent \begin{minipage}{0.87\linewidth} \footnotesize #1 \end{minipage} \\[0.1cm]
}

\newcommand\createskill[2]{%
    \textbf{#1} & #2
}

\newcommand\createskills[2]{%
  \explanationdetail{%
    \hspace{-1mm}\begin{tabularx}{\textwidth}{@{} p{0.125\textwidth} X @{}}
      \makeatletter
      \@for\thisitem:=#1\do{%
        \thisitem\\[0.1cm]
      }
      \makeatother
    \end{tabularx}
  }%
}
