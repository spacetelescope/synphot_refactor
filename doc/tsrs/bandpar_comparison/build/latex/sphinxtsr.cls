%
% tsr.cls for Sphinx
%
% A class for generating Technical Software Reports
%
% Based on the howto class in Sphinx
%

\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{tsr}[2009/11/25 TSR class]

% Pass all given class options to the parent class.
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{howto}}
\ProcessOptions\relax
\LoadClass{sphinxhowto}

\newcommand{\TSR}{}

% Change the title page to look a bit better, and fit in with the fncychap
% ``Bjarne'' style a bit better.
%
\renewcommand{\maketitle}{
  \rule{\textwidth}{1pt}
  \ifsphinxpdfoutput
    \begingroup
    % This \def is required to deal with multi-line authors; it
    % changes \\ to ', ' (comma-space), making it pass muster for
    % generating document info in the PDF file.
    \def\\{, }
    \pdfinfo{
      /Author (\@author)
      /Title (\@title)
    }
    \endgroup
  \fi
  \begin{flushleft}
    \begin{tabular}{p{3in}l}
      \includegraphics[width=2.5in]{stsci_logo.pdf} &
      {\rm\Large Technical Software Report \version} \par \\
    \end{tabular}
    \vspace{16pt} \par
    {\rm\Huge\py@HeaderFamily \@title} \par
    \vspace{12pt} \par
    \hspace{3.20in} \rule{1.5in}{1pt} \par
    \vspace{12pt}
    \begin{tabular}{p{3in}p{3.15in}}
      & {\large \@author} \\
      & {\large \@date} \\
    \end{tabular}
  \end{flushleft}
  \@thanks
  \setcounter{footnote}{0}
  \let\thanks\relax\let\maketitle\relax
  %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
}

