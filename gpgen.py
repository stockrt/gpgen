#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 * =========================================================================
 * gpgen.py
 * -------------------------------------------------------------------------
 * DESCRIPTION:   Generate static index.html for GitHub Pages based on
 *                user-defined template.
 *
 * AUTHOR:        (rcs) Rogério Carvalho Schneider <stockrt@gmail.com>
 *                http://stockrt.github.com
 * =========================================================================
'''

### DEFINES_START ###
# --------------------------------------------------------------------------
# Set this values
# You should change this values to fit your needs and your personal data, so
# you can provide projects you do not want to list, or change the suggested
# descriptions. I recommend changing most of the bellow.

# Your github login
login = 'stockrt'

# Include or not private repositories?
include_private_repos = True

# The projects you do not want to list in your page
exclude_projects = [login + '.github.com', 'packages', 'testproject']

# HTML contents
page = {'html_head_title': 'Weekend codes',
        'html_head_description': 'Codes and random stuff I am up to share with you',
        'html_head_keywords': 'python, github user page, weekend codes, modules, rpm, linux',
        'html_body_message': 'and here you can find some of my weekend codes:'
}

# Extra Footer links
extra_footer_links = []
extra_footer_links.append({'url': 'http://%s.github.com' % login,
                    'description': 'home'})
extra_footer_links.append({'url': 'http://github.com/%s/packages' % login,
                    'description': 'packages'})
extra_footer_links.append({'url': 'http://twitter.com/%s' % login,
                    'description': 'twitter'})
extra_footer_links.append({'url': 'http://stockrtweb.homelinux.com',
                    'description': 'directory listing at home'})
extra_footer_links.append({'url': 'http://%s.github.com/misc/vitae/rogerio_schneider.pdf' % login,
                    'description': 'vitae'})
extra_footer_links.append({'url': 'http://picasaweb.google.com/%s' % login,
                    'description': 'seeme'})

# Your google-analytics javascript
google_analytics_js = '''
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-5567404-4");
pageTracker._trackPageview();
} catch(err) {}
</script>
'''
# Set this values
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Change this HTML template if you want
# You could, for instance, need to use an external CSS, or to change some
# definition I put here, so, feel free to change it as you want, this is only
# a suggestion, but an working one.
template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>${user['name']} - ${page['html_head_title']}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="author" content="${user['name']}" xml:lang="en" lang="en"/>
<meta name="description" content="${page['html_head_description']}" xml:lang="en" lang="en"/>
<meta name="keywords" content="${page['html_head_keywords']}" xml:lang="en" lang="en"/>

<!-- Style -->
<style type="text/css">
* {
    margin: 0;
    padding: 0;
}
h1 {
    font-weight: normal;
    margin-bottom: 30px;
    color: #222;
    font-size: 35px;
}
h2 {
    font-weight: normal;
    margin-bottom: 30px;
    color: #222;
    font-size: 30px;
}
body {
    font-family: 'Palatino Linotype', Palatino, Georgia, 'Times New Roman',
    serif;
    background-color: #fff;
    overflow: auto;
    font-size: 20px;
    width:750px;
    margin:0 auto;
    margin-top:30px;
}
a {
    text-decoration: none;
    color: #777;
}
a:hover {color: #444;}
img#forkme {
    position: absolute;
    top: 0;
    right: 0;
    border: 0;
}
#container {
    width: 500pt;
    text-align: center;
    margin-top: 100px;
}
#repositories {
    width: 500pt;
    text-align: center;
    margin-top: 100px;
}
#footer {
    margin-top: 100px;
}
</style>
<!-- /Style -->

</head>

<body>
<a href="http://github.com/${login}"><img id="forkme"
src="forkme_right_orange.png" alt="Fork me on GitHub"/></a>

<div id="container">
    <h1>Hi</h1>
    <h1>I'm <strong>${user['name']}</strong></h1>
    <h2>${page['html_body_message']}</h2>
    <br/>

    <div id="repositories"></div>
        % for repo in repositories:
            <li><a href="${repo['url']}">${repo['name']}</a> - ${repo['description']}</li><br/>
        % endfor
    <br/>

    <div id="footer">
        <a href="http://github.com/${login}">projects</a> |
        % for link in extra_footer_links:
            <a href="${link['url']}">${link['description']}</a> |
        % endfor
        <a href="mailto:${user['email']}">reachme</a>
    </div>
    <br/>
</div>
${google_analytics_js}
<!-- ${generated} -->
</body>
</html>'''
# Change this HTML template if you want
# --------------------------------------------------------------------------
### DEFINES_END ###

### GENERIC_SETUP_MARKER_START ###
__program_file__     = 'gpgen.py'
__program_name__     = '%s' % __program_file__.split('.py')[0]
__scripts__          = [__program_file__]
__data_files__       = [('/usr/bin', [__program_file__])]
__version__          = '0.1.1'
__date__             = '2009/07/19'
__author_email__     = 'stockrt@gmail.com'
__author__           = 'Rogério Carvalho Schneider <%s>' % __author_email__
__maintainer_email__ = __author_email__
__maintainer__       = __author__
__copyright__        = 'Copyright (C) 2009 Rogério Carvalho Schneider'
__license__          = 'GPLv3'
__url__              = 'http://stockrt.github.com'
__download_url__     = __url__
__py_modules__       = []
__platforms__        = ['any']
__keywords__         = 'github page gen index.html'
__classifiers__      = ['Development Status :: 1 - Planning',
'Environment :: Web Environment',
'Intended Audience :: End Users/Desktop',
'License :: OSI Approved :: GNU General Public License (GPL)',
'Operating System :: OS Independent',
'Programming Language :: Python',
'Topic :: Utilities']
__description__      = 'Generate static index.html for GitHub Pages'
__long_description__ = '''%s
Generate static index.html for GitHub Pages based on
user-defined template.
''' % __program_file__
__rpm_data__        = '''
%files
%defattr(-,root,root,-)
/usr/bin/%{name}.py
@@PYLIB_MARKER@@/%{name}-%{unmangled_version}-py@@PYVER_MARKER@@.egg-info
'''
### GENERIC_SETUP_MARKER_END ###

### IMPORTS_START ###
import sys
try:
    from mako.template import Template
    import simplejson
except ImportError, why:
    print
    print 'Error loading module: [%s]' % why
    print '''
You need to install some extra modules in order to run this program.
Please read Installation Notes:

# Installation Notes:
- You will need some extra modules to put this thing to work. Here is how to
get them:
 wget http://peak.telecommunity.com/dist/ez_setup.py
 python ez_setup.py
 easy_install mako
 easy_install simplejson
'''
    sys.exit(-1)
import optparse
import urllib2
import time
### IMPORTS_END ###

##########
## MAIN ##
##########
def main():
    # Parse possible options
    usage = 'usage: %prog [options] <file>'
    version = 'version: %s %s' % (__program_name__, __version__)
    parser = optparse.OptionParser(usage=usage, version=version)
    parser.add_option('-g', '--gen',
            help='Generates the static html for GitHub [default: %default]')
    parser.set_defaults(gen='index.html')
    (options, args) = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        print
        print 'Also, you may need to edit this script and change some values \
to fit your preferences'
        parser.exit(1)

    # Get data from GitHub
    github_api_url = 'http://github.com/api/v2/json'

    print 'Getting user\'s profile (%s)...' % login
    json = urllib2.urlopen(github_api_url + '/user/show/' + login).read()
    user = simplejson.loads(json)['user']
    print 'Getting user\'s profile (%s)... done' % login

    print 'Getting user\'s repositories (%s)...' % login
    json = urllib2.urlopen(github_api_url + '/repos/show/' + login).read()
    repos = simplejson.loads(json)['repositories']
    print 'Getting user\'s repositories (%s)... done' % login

    # Remove unwanted repos
    repos2 = []
    for r in repos:
        if (r['private'] and not include_private_repos) or \
        (r['name'] in exclude_projects):
            continue
        repos2.append(r)

    # Sort repos
    repositories = []
    l = [r['name'] for r in repos2]
    l.sort()
    for n in l:
        for r in repos2:
            if r['name'] == n:
                repositories.append(r)
                break

    # Generation time
    generated = 'Generated by %s on %s (%s)' % (__program_name__,
                                                time.ctime(),
                                                __url__)

    # Generate output based on the defined template
    t = Template(template)
    t2 = t.render_unicode(login=login,
                          page=page,
                          extra_footer_links=extra_footer_links,
                          google_analytics_js=google_analytics_js,
                          generated=generated,
                          user=user,
                          repositories=repositories)
    print 'Writing output to %s file...' % options.gen
    open(options.gen, 'w').write(t2.encode('utf-8', 'replace'))
    print 'Writing output to %s file... done' % options.gen

if __name__ == '__main__':
    main()
