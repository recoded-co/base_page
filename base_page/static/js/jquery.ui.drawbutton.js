/*
Draw Button is a drawing
tool that works together with
Openlayers.

Required global variables is a
OpenLayers map object with the
button required draw controls.

control : The id of the map control to use
classes : The classes to add to the widget on initialization
text_class: the class to be added to the span that includes the button text
active_class: the class to use when a button is activated
*/
(function( $ ) {
    $.widget("ui.drawButton",
        {
            options: {
                drawcontrol: "drawcontrol", //the draw control used, required
                selectcontrol: "selectcontrol",
                classes: "ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only",
                text_class: "ui-button-text",
                active_class: "ui-state-active",
                disable_class: "ui-button-disabled ui-state-disabled",
                rule_added: false,
                icons: {
                    primary: undefined,
                    secondary: undefined
                }
            },
            _create: function() {
                this.element.addClass( this.options.classes )
                this.element.bind('click',
                          this.toggle_active);
                var label = this.element.html();
                $( "<span></span>")
                        .addClass( this.options.text_class )
                        .appendTo( this.element.empty() )
                        .html( label )
                        .text();
                
                return this;
            },

            toggle_active: function(evt) {
                var active_cls = $(this).drawButton('option', 'active_class');
                if($(this).hasClass( active_cls )) {
                    $(this).drawButton('deactivate');
                } else {
                    $(this).drawButton('activate');
                }
            },
            deactivate: function() {
                this.element.removeClass( this.options['active_class'] );
                var drawcontrol_id = this.options['drawcontrol'];
                var drawcontrol = map.getControl(drawcontrol_id);
                drawcontrol.deactivate();
                var selectcontrol_id = this.options['selectcontrol'];
                var selectcontrol = map.getControl(selectcontrol_id);
                selectcontrol.activate();
            },
            activate: function() {
                if(this.element.attr( 'disabled') !== 'disabled') {
                    
                    //unselect the others
                    $(".drawbutton." + this.options['active_class'])
                        .drawButton( 'deactivate' );
                    this.element.addClass( this.options['active_class'] );
                    var drawcontrol_id = this.options['drawcontrol'];
                    var drawcontrol = map.getControl(drawcontrol_id);
                    drawcontrol.activate();
                    var selectcontrol_id = this.options['selectcontrol'];
                    var selectcontrol = map.getControl( selectcontrol_id );
                    selectcontrol.deactivate();
                    
                    //change the temporary style of the layer
                    var color = $(this.element).data('color');
                    var name = $(this.element).attr('name');
                    if(!this.options.rule_added) {
                        var rule = new OpenLayers.Rule({
                                    filter: new OpenLayers.Filter.Comparison({
                                        type: OpenLayers.Filter.Comparison.EQUAL_TO,
                                        property: 'name',
                                        value: name
                                    }),
                                    symbolizer: {
                                        externalGraphic: '/images/needle?color=' + color,
                                        graphicHeight: 36,
                                        graphicWidth: 23,
                                        graphicYOffset: -30,
                                        cursor: 'pointer'
                                        }
                                    });                        
                        drawcontrol.layer.styleMap.styles.default.addRules([rule]);
                        this.options.rule_added = true;
                    }
                    drawcontrol.layer.styleMap.styles.temporary.defaultStyle.externalGraphic = '/images/needle?color=' + color;
                }
            },
            disable: function() {
                this.element.removeClass( this.options['active_class'] );
                this.element.addClass( this.options['disable_class'] );
                this.element.attr( 'disabled', 'disabled');
                var drawcontrol_id = this.options['drawcontrol'];
                var drawcontrol = map.getControl(drawcontrol_id);
                drawcontrol.deactivate();
                var selectcontrol_id = this.options['selectcontrol'];
                var selectcontrol = map.getControl(selectcontrol_id);
                selectcontrol.activate();
            },
            enable: function() {
                this.element.removeClass( this.options['disable_class'] );
                this.element.removeAttr( 'disabled' );
            }
        });
})( jQuery );