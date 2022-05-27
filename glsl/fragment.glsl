varying vec2 pos;
            
uniform sampler2D s_texture;
uniform float texture_width;
uniform float texture_height;

void main() {
    float tx = pos.x;
    float ty = pos.y;
    float dx = 1.0 / texture_width;
    float dy = 1.0 / texture_height;
    

    vec4 v1 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, -dy ) );
    vec4 v2 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, 0 ) );
    vec4 v3 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, dy ) );
    
    vec4 v4 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, -dy ) );
    vec4 v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , 0 ) );
    vec4 v6 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, dy ) );
    
    vec4 v7 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, -dy ) );
    vec4 v8 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, 0 ) );
    vec4 v9 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, dy ) );
    
    gl_FragColor = texture2D(s_texture, vec2( tx, ty ));
    
    vec4 final_color = ( v1 + v2 + v3 + v4 + v5 + v6 + v7 +v8 + v9) / 9.0;
    gl_FragColor = clamp(abs(v5 - final_color) * 100.0, vec4(0,0,0,0), vec4(1,1,1,1)) ;
}