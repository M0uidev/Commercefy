from django import template

register = template.Library()

@register.inclusion_tag('components/card.html', takes_context=True)
def ui_card(context, title=None, icon=None, extra_classes=''):
    """
    Renders a standardized card component.
    Usage:
    {% ui_card title="My Title" icon="bi-star" %}
        Content here...
    {% endui_card %}
    Note: Since this is an inclusion tag, it doesn't support block content directly in the standard way 
    unless we use a custom tag parser or pass content as variable. 
    However, for a wrapper, a custom block tag is better, or just a simple include with 'with'.
    
    But to keep it simple and Pythonic as requested:
    Let's make it a simple inclusion tag that expects 'content' in context if used that way, 
    but standard Django tags don't work like wrappers easily without 'endtag'.
    
    So, let's use a custom template tag that parses until end tag.
    """
    return {
        'title': title,
        'icon': icon,
        'extra_classes': extra_classes,
    }

@register.tag(name="ui_block")
def do_ui_block(parser, token):
    """
    Block tag to wrap content in a standardized card.
    Usage:
    {% ui_block title="My Title" icon="bi-star" %}
        HTML content...
    {% endui_block %}
    """
    nodelist = parser.parse(('endui_block',))
    parser.delete_first_token()
    
    # Parse arguments
    args = token.split_contents()[1:]
    kwargs = {}
    for arg in args:
        if '=' in arg:
            k, v = arg.split('=', 1)
            kwargs[k] = v.strip('"\'')
            
    return UiBlockNode(nodelist, **kwargs)

class UiBlockNode(template.Node):
    def __init__(self, nodelist, title=None, icon=None, extra_classes=''):
        self.nodelist = nodelist
        self.title = title
        self.icon = icon
        self.extra_classes = extra_classes

    def render(self, context):
        content = self.nodelist.render(context)
        
        # Resolve variables if they are template variables
        title = self.title
        if title:
            try:
                title = template.Variable(title).resolve(context)
            except template.VariableDoesNotExist:
                pass # Keep as string literal
                
        output = f"""
        <div class="dash-card p-4 {self.extra_classes}">
        """
        
        if title:
            icon_html = f'<i class="bi {self.icon} me-2"></i>' if self.icon else ''
            output += f"""
            <div class="d-flex align-items-center mb-4 border-bottom pb-3">
                <h2 class="h4 fw-bold mb-0 text-main">{icon_html}{title}</h2>
            </div>
            """
            
        output += f"""
            <div class="card-content">
                {content}
            </div>
        </div>
        """
        return output
